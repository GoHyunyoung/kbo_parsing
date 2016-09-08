package link.springapp.mvc.repository;

import link.springapp.mvc.domain.winlosePitcher;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

public interface winlosePitcherMapper {
    @Select("SELECT * FROM winlosePitcher WHERE id = #{ArticleId}")
    winlosePitcher getWinlosePitcher(@Param("ArticleId") int ArticleId);
}
