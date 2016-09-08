package link.springapp.mvc.controller;
import link.springapp.mvc.domain.Article;
import link.springapp.mvc.domain.CriticalVOD_Url;
import link.springapp.mvc.domain.winlosePitcher;
import link.springapp.mvc.service.ArticleService;
import link.springapp.mvc.service.CriticalVOD_UrlService;
import link.springapp.mvc.service.winlosePitcherService;
import org.apache.commons.logging.impl.Log4JLogger;
import org.apache.ibatis.logging.Log;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.ArrayList;
import java.util.Deque;

import static link.springapp.mvc.service.winlosePitcherService.*;

@Controller
@Transactional
@RequestMapping("/")
public class HelloController {
    private Logger logger= Logger.getLogger(this.getClass());

    @Autowired
    private ArticleService articleService;
    @Autowired
    private CriticalVOD_UrlService CriticalVOD_UrlService;
    @Autowired
    private winlosePitcherService winlosePitcherService;

    @RequestMapping(value = {"/", "/index"}, method = RequestMethod.GET)
    public String printWelcome(ModelMap model) {
        logger.info("-----BEGIN /index CONTROLLER-----");
        logger.info("-----END /index CONTROLLER-----");
        return "index";
    }

    @RequestMapping(value = {"/timeline"}, method = RequestMethod.GET)
    public String printTimeline(ModelMap model) {
        logger.info("-----BEGIN /timeline CONTROLLER-----");
        ArrayList<Article> articleArrayList = new ArrayList<>();
//        Deque urlArrayDeque<CriticalVOD_Url> urlArrayDeque = new Deque<>();
//        int[] urlCountArr= new int[10];
        int articleCount = articleService.getArticleCount();

        for (int i = 0; i < 10; i++) {
            Article article = articleService.getArticle(articleCount-i);
            articleArrayList.add(article);
//            CriticalVOD_Url[] criticalVOD_url = CriticalVOD_UrlService.getCriticalVOD_Url(article.getId());
//            urlCountArr[i]=criticalVOD_url.length;
            }
        model.addAttribute("articleArrayList", articleArrayList);
//        model.addAttribute("urlArrayList",UrlArrayList);
//        model.addAttribute("urlCountArr",urlCountArr);
        logger.info("-----END /timeline CONTROLLER-----");
        return "timeline";
    }

    @RequestMapping(value = "/scroll", method = RequestMethod.GET)
    public String getMoreArticle(ModelMap model,@RequestParam("articleId")
        int articleId,@RequestParam("sequence") String sequence) {

        logger.info("-----BEGIN /scroll CONTROLLER-----");
        ArrayList<Article> articleArrayList = new ArrayList<>();
        ArrayList<CriticalVOD_Url> UrlArrayList = new ArrayList<>();
        logger.info("----- WORKING 1 -----");
        logger.info("articleId="+articleId);
        logger.info("sequence="+sequence);

//      lastIndex설정
        for (int i = 0; i < 10; i++) {
//          RECENT->OLD 글 순서
            int index=i;
            if (sequence.equals("DESC"))index*= -1;
            logger.info("for LOOP i = "+i);
            if(articleService.getArticle(articleId + index)==null)
                break;
            Article article = articleService.getArticle(articleId+index);
            articleArrayList.add(article);
        }

        logger.info("Error? : WORKING 2");
        model.addAttribute("articleArrayList", articleArrayList);
        model.addAttribute("UrlArrayList", UrlArrayList);
        logger.info("-----END /scroll CONTROLLER-----");
        return "scroll";
    }

    @RequestMapping(value = "/search", method = RequestMethod.GET)
    public String getSearchResult(ModelMap model, @RequestParam(value = "searchDate") String searchDate) {
        int searchResultMinId = articleService.getSearchResultMinId(searchDate);

        logger.info("-----BEGIN /search CONTROLLER-----");
        ArrayList<Article> articleArrayList = new ArrayList<>();
        logger.info("----- WORKING 1 -----");
        logger.info("searchDate="+searchDate);

//      lastIndex설정
        for (int i = 0; i < 10; i++) {
//          RECENT->OLD 글 순서
            logger.info("for LOOP i = "+i);
            if(articleService.getArticle(searchResultMinId + i)==null)
                break;
            Article article = articleService.getArticle(searchResultMinId+i);
            articleArrayList.add(article);
        }

        logger.info("WORKING 2");
        model.addAttribute("articleArrayList", articleArrayList);
        logger.info("-----END /search CONTROLLER-----");
        return "search";
    }

    @RequestMapping(value = {"/boxscore"}, method = RequestMethod.GET)
    public String getGameData(ModelMap model) {
        logger.info("-----BEGIN /gamePicker CONTROLLER-----");
        logger.info("-----END /gamePicker CONTROLLER-----");
        return "boxscore";
    }

    @RequestMapping(value = {"/gamePicker"}, method = RequestMethod.GET)
    public String selectGamePicker(ModelMap model, @RequestParam(value = "gameDate") String gameDate) {
        int searchResultMinId = articleService.getSearchResultMinId(gameDate);

        logger.info("-----BEGIN /gamePicker CONTROLLER-----");
        ArrayList<Article> articleArrayList = new ArrayList<>();
        logger.info("----- WORKING 1 -----");
        logger.info("gameDate="+gameDate);

        for (int i = 0; i < 6; i++) {
            logger.info("for LOOP i = "+i);
            if(articleService.getArticle(searchResultMinId + i)==null)
                break;
            Article article = articleService.getArticle(searchResultMinId+i);
            articleArrayList.add(article);
        }

        logger.info("WORKING 2");
        model.addAttribute("articleArrayList", articleArrayList);

        logger.info("-----END /gamePicker CONTROLLER-----");
        return "gamePicker";
    }

    @RequestMapping(value = {"/gamebox"}, method = RequestMethod.GET)
    public String getGameBox(ModelMap model,@RequestParam("articleId") int articleId) {
        logger.info("-----BEGIN /gamebox CONTROLLER-----");

        ArrayList<Article> articleArrayList = new ArrayList<>();
        ArrayList<winlosePitcher> WinlosePitcherArrayList = new ArrayList<>();

        Article article = articleService.getArticle(articleId);
        articleArrayList.add(article);
        model.addAttribute("articleArrayList", articleArrayList);

        winlosePitcher WinlosePitcher = winlosePitcherService.getWinlosePitcher(articleId);
        WinlosePitcherArrayList.add(WinlosePitcher);
        model.addAttribute("WinlosePitcherArrayList", WinlosePitcherArrayList);

        logger.info("-----END /gamebox CONTROLLER-----");
        return "gamebox";
    }

    @RequestMapping(value = {"/teampage"}, method = RequestMethod.GET)
    public String getTeamPage(ModelMap model) {
        logger.info("-----BEGIN /teampage CONTROLLER-----");
        logger.info("-----END /teampage CONTROLLER-----");
        return "teampage";
    }
}
