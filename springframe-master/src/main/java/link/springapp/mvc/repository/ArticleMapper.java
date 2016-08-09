package link.springapp.mvc.repository;

import link.springapp.mvc.domain.Article;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

public interface ArticleMapper {
    @Select("SELECT * FROM Article WHERE id = #{ArticleId}")
    Article getArticle(@Param("ArticleId") int ArticleId);

    @Select("SELECT COUNT(*) FROM Article")
    int getArticleCount();

    @Select("call searchArticle_FromDate(#{searchDate})")
    Article[] getSearchResult(@Param("searchDate")String searchDate);

}
