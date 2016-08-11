package link.springapp.mvc.controller;

import link.springapp.mvc.domain.Article;
import link.springapp.mvc.service.ArticleService;
import org.omg.CORBA.Object;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

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
        int articleCount=articleService.getArticleCount();
        int lastIndex=0;

        for (int i = 0; i < 10; i++) {
//        lastIndex설정
            if(articleService.getArticle(articleCount-startId-i)==null)
                break;
            lastIndex++;
        }
        Article[] articleList = new Article[lastIndex];
        for (int i = 0; i < articleList.length; i++) {
            articleList[i] = articleService.getArticle(articleCount-startId-i);
        }

        model.addAttribute("articleList", articleList);
        return "scroll";
    }

    @RequestMapping(value = "/search",method = RequestMethod.GET)
    public String getSearchResult(ModelMap model,@RequestParam(value = "searchDate")String searchDate){
        Article[] searchResult = new Article[10];
        int searchResultCount=articleService.getSearchCount(searchDate);
        for(int i=0;i<searchResult.length;i++) {
            if(articleService.getSearchResult(searchDate)[searchResultCount - i]!=null)
                searchResult[i] = articleService.getSearchResult(searchDate)[searchResultCount - i];
        }
        model.addAttribute("searchResult",searchResult);

        return "search";
    }
}