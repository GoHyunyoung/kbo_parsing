package link.springapp.mvc.repository;

import link.springapp.mvc.domain.CriticalVOD_Url;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

public interface CriticalVOD_UrlMapper {
    @Select("SELECT * FROM CriticalVOD_Url WHERE Article_Id = #{ArticleId}")
    CriticalVOD_Url[] getCriticalVOD_Url(@Param("ArticleId") int ArticleId);

    @Select("SELECT COUNT(*) FROM CriticalVOD_Url")
    int getCriticalVOD_UrlCount();
}
