package link.springapp.mvc.controller;

import link.springapp.mvc.domain.Article;
import link.springapp.mvc.service.ArticleService;
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

@Controller
@Transactional
@RequestMapping("/")

public class HelloController {
    private Logger logger= Logger.getLogger(this.getClass());

    @Autowired
    private ArticleService articleService;

    @RequestMapping(value = "/", method = RequestMethod.GET)
    public String printWelcome(ModelMap model) {
        logger.info("-----BEGIN index CONTROLLER-----");

        ArrayList<Article> articleArrayList = new ArrayList<>();

        int articleCount = articleService.getArticleCount();

        for (int i = 0; i < 10; i++) {
            Article article = articleService.getArticle(articleCount-i);
            articleArrayList.add(article);
        }
        model.addAttribute("articleArrayList", articleArrayList);
        logger.info("-----END index CONTROLLER-----");

        return "index";
    }

    @RequestMapping(value = "/scroll", method = RequestMethod.GET)
    public String getMoreArticle(ModelMap model,@RequestParam("articleId") int articleId,@RequestParam("sequence") String sequence) {
        logger.info("-----BEGIN /scroll CONTROLLER-----");

        ArrayList<Article> articleArrayList = new ArrayList<>();
        logger.info("----- WORKING 1 -----");
        logger.info("articleId="+articleId);
        logger.info("sequence="+sequence);

//        lastIndex설정
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

        logger.info("WORKING 2");

        model.addAttribute("articleArrayList", articleArrayList);

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
}