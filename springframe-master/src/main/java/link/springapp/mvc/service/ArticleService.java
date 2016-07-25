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
    public int getArticleLength(){
        int length = articleMapper.getArticleLength();
        return length;
    }
}