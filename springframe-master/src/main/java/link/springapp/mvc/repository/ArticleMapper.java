package link.springapp.mvc.repository;

import link.springapp.mvc.domain.Article;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

public interface ArticleMapper {
    @Select("SELECT * FROM Article WHERE id = #{ArticleId}")
    Article getArticle(@Param("ArticleId") int ArticleId);

    @Select("SELECT awayT FROM Article WHERE id = #{ArticleId}")
    String getawayT(@Param("ArticleId") int ArticleId);

    @Select("SELECT homeT FROM Article WHERE id = #{ArticleId}")
    String gethomeT(@Param("ArticleId") int ArticleId);

//    @Select("SELECT * FROM Article WHERE id = #{ArticleId} LIMIT 10")
//    Article[] getArticleArray(@Param("ArticleId") int ArticleId);

    @Select("SELECT COUNT(*) FROM Article")
    int getArticleCount();

    @Select("SELECT MIN(Article.id) FROM Article WHERE date >= #{searchDate}")
    int getSearchResultMinId(@Param("searchDate") String searchDate);

//    @Select("call searchArticle_FromDate(#{searchDate})")
//    Article[] getSearchResult(@Param("searchDate") String searchDate);
}