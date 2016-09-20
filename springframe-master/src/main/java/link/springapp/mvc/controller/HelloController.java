package link.springapp.mvc.controller;
import link.springapp.mvc.domain.Article;
import link.springapp.mvc.domain.CriticalVOD_Url;
import link.springapp.mvc.domain.WinLosePitcher;
import link.springapp.mvc.service.ArticleService;
import link.springapp.mvc.service.CriticalVOD_UrlService;
import link.springapp.mvc.service.WinLosePitcherService;
import org.apache.log4j.Logger;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import java.util.ArrayList;

@Controller
@Transactional
@RequestMapping("/")
public class HelloController {
    private Logger logger= Logger.getLogger(this.getClass());

    @Autowired
    private ArticleService articleService;
    @Autowired
    private CriticalVOD_UrlService criticalVOD_UrlService;
    @Autowired
    private WinLosePitcherService winlosePitcherService;

    @RequestMapping(value = {"/", "/index"}, method = RequestMethod.GET)
    public String printWelcome(ModelMap model) {
        logger.info("-----/index CONTROLLER-----");
        return "index";
    }

    @RequestMapping(value = {"/timeline"}, method = RequestMethod.GET)
    public String printTimeline(ModelMap model) {
        logger.info("-----BEGIN /timeline CONTROLLER-----");
        ArrayList<Article> articleArrayList = new ArrayList<>();
        int[] urlCountArr= new int[10];
        int articleCount = articleService.getArticleCount();
        ArrayList<CriticalVOD_Url> criticalVOD_urlArrayList = new ArrayList<>();

        for (int i = 0; i < 10; i++) {
            Article article = articleService.getArticle(articleCount-i);
            articleArrayList.add(article);
            urlCountArr[i]=criticalVOD_UrlService.getCriticalVOD_Url(article.getId()).size();
            for(CriticalVOD_Url instance:criticalVOD_UrlService.getCriticalVOD_Url(article.getId()))
                criticalVOD_urlArrayList.add(instance);
        }

        model.addAttribute("articleArrayList", articleArrayList);
        model.addAttribute("criticalVOD_urlArrayList", criticalVOD_urlArrayList);
        model.addAttribute("urlCountArr",urlCountArr);
        logger.info("-----END /timeline CONTROLLER-----");
        return "timeline";
    }

    @RequestMapping(value = "/scroll", method = RequestMethod.GET)
    public String getMoreArticle(ModelMap model,@RequestParam("articleId")
            int articleId,@RequestParam("sequence") String sequence) {

        logger.info("-----BEGIN /scroll CONTROLLER-----");
        ArrayList<Article> articleArrayList = new ArrayList<>();
        ArrayList<CriticalVOD_Url> UrlArrayList = new ArrayList<>();
        ArrayList<CriticalVOD_Url> criticalVOD_urlArrayList = new ArrayList<>();
        int[] urlCountArr= new int[10];
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
            urlCountArr[i]=criticalVOD_UrlService.getCriticalVOD_Url(article.getId()).size();
            for(CriticalVOD_Url instance:criticalVOD_UrlService.getCriticalVOD_Url(article.getId()))
                criticalVOD_urlArrayList.add(instance);
        }

        model.addAttribute("articleArrayList", articleArrayList);
        model.addAttribute("criticalVOD_urlArrayList", criticalVOD_urlArrayList);
        model.addAttribute("UrlArrayList", UrlArrayList);
        model.addAttribute("urlCountArr",urlCountArr);
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
        logger.info("-----/gamePicker CONTROLLER-----");
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
        ArrayList<WinLosePitcher> winlosePitcherArrayList = new ArrayList<>();

        Article article = articleService.getArticle(articleId);
        articleArrayList.add(article);
        model.addAttribute("articleArrayList", articleArrayList);

        WinLosePitcher winlosePitcher = winlosePitcherService.getWinlosePitcher(articleId);
        winlosePitcherArrayList.add(winlosePitcher);
        model.addAttribute("WinlosePitcherArrayList", winlosePitcherArrayList);

        logger.info("-----END /gamebox CONTROLLER-----");
        return "gamebox";
    }

    @RequestMapping(value = {"/teampage"}, method = RequestMethod.GET)
    public String getTeamPage(ModelMap model) {
        logger.info("-----/teampage CONTROLLER-----");
        return "teampage";
    }

    @RequestMapping(value = {"/teamArticle"}, method = RequestMethod.GET)
    public String getTeamArticle(ModelMap model,@RequestParam(value = "teamName") String teamName) {
        logger.info("-----BEGIN /teamArticle CONTROLLER-----");

        int articleCount = articleService.getArticleCount();
        ArrayList<Article> articleArrayList = new ArrayList<>();

        for (int i = 0; i < 30; i++) {
            Article article = articleService.getArticle(articleCount-i);
            if (teamName.equals(articleService.getawayT(articleCount-i)) ||
                    teamName.equals(articleService.gethomeT(articleCount-i)) ) {
                articleArrayList.add(article);
            }
        }

        model.addAttribute("articleArrayList", articleArrayList);
        logger.info("-----END /teamArticle CONTROLLER-----");
        return "teamArticle";
    }
}