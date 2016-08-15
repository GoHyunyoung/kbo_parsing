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
        ArrayList<Article> articleArrayList = new ArrayList<>();

        int articleCount = articleService.getArticleCount();

        for (int i = 0; i < 10; i++) {
            Article article = articleService.getArticle(articleCount-i);
            articleArrayList.add(article);
        }
        model.addAttribute("articleArrayList", articleArrayList);
        return "index";
    }

    @RequestMapping(value = "/scroll", method = RequestMethod.GET)
    public String getMoreArticle(ModelMap model, @RequestParam(value = "articleId") int articleId,@RequestParam(value= "sequence") String sequence) {

        ArrayList<Article> articleArrayList = new ArrayList<>();

//        lastIndex설정
        for (int i = 0; i < 10; i++) {
//          RECENT->OLD 글 순서
            if(articleService.getArticle(articleId + i)==null)
                break;
            if (sequence.equals("DESC")) i *= -1;
            else {
                Article article = articleService.getArticle(articleId+i);
                articleArrayList.add(article);
            }
        }
        model.addAttribute("articleArrayList", articleArrayList);
        System.out.println(articleArrayList);

        logger.info("123");
        return "scroll";
    }

    @RequestMapping(value = "/search", method = RequestMethod.GET)
    public String getSearchResult(ModelMap model, @RequestParam(value = "searchDate") String searchDate) {
        int searchResultMinId = articleService.getSearchResultMinId(searchDate);
        int arrLength = 0;
        for (int i = 0; i < 10; i++) {
//        lastIndex설정
            if (articleService.getArticle(searchResultMinId + i) == null)
                break;
            arrLength++;
        }
        Article[] searchResult = new Article[arrLength];
        for (int i = 0; i < searchResult.length; i++) {
            searchResult[i] = articleService.getArticle(searchResultMinId + i);
        }
        model.addAttribute("searchResult", searchResult);
        return "search";
    }
}