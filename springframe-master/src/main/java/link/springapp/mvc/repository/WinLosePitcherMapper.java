package link.springapp.mvc.repository;

import link.springapp.mvc.domain.WinLosePitcher;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

public interface WinLosePitcherMapper {
    @Select("SELECT * FROM winlosePitcher WHERE id = #{ArticleId}")
    WinLosePitcher getWinlosePitcher(@Param("ArticleId") int ArticleId);
}
