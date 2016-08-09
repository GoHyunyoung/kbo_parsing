package link.springapp.mvc.service;

import link.springapp.mvc.domain.Article;
import link.springapp.mvc.repository.ArticleMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class ArticleService {
    @Autowired
    private ArticleMapper articleMapper;

    public Article getArticle(int id) {
        Article article = articleMapper.getArticle(id);
        return article;
    }
    public int getArticleCount(){
        int count = articleMapper.getArticleCount();
        return count;
    }
    public int getSearchCount(String searchDate){
        int count = articleMapper.getSearchResult(searchDate).length;
        return count;
    }
    public Article[] getSearchResult(String searchDate){
        Article[] article =  articleMapper.getSearchResult(searchDate);
        return article;
    }
}