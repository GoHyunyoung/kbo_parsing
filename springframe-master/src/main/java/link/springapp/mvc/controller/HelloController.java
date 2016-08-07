package link.springapp.mvc.controller;

import link.springapp.mvc.domain.Article;
import link.springapp.mvc.service.ArticleService;
import org.apache.ibatis.annotations.Select;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import java.io.Console;
import java.util.ArrayList;
import java.util.HashMap;

@Controller
@Transactional
@RequestMapping("/")
public class HelloController {
    @Autowired
    private ArticleService articleService;
    @RequestMapping(value = "/", method = RequestMethod.GET)
    public String printWelcome(ModelMap model) {
        Article[] articleList = new Article[10];
        int articleCount=articleService.getArticleCount();
        for (int i = 0; i<articleList.length; i++) {
            articleList[i] = articleService.getArticle(articleCount-i);
        }

        model.addAttribute("articleList", articleList);
        return "index";
    }

    @RequestMapping(value = "/scroll", method = RequestMethod.GET)
    public String getMoreArticle(ModelMap model, @RequestParam(value = "articleId")int startId) {
        Article[] articleList = new Article[10];
        int articleCount=articleService.getArticleCount();

        for (int i = 0; i < articleList.length; i++) {
            articleList[i] = articleService.getArticle(articleCount-startId-i);
        }
        model.addAttribute("articleList", articleList);
        return "scroll";
    }

    @RequestMapping(value = "/search.jsp",method = RequestMethod.GET)
    public String getSearchResult(ModelMap model,
                                  @RequestParam(value = "searchingYear")String searchingYear,
                                  @RequestParam(value = "searchingMonth")String searchingMonth,
                                  @RequestParam(value = "searchingDay")String searchingDay) {
//        HashMap<String,Object> searchingMap = new HashMap<>();
//        Article article = articleService.getSearchResult();
//        }
        return "search";
    }
}