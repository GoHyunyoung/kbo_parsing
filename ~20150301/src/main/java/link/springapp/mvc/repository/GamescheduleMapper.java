package link.springapp.mvc.repository;

import link.springapp.mvc.domain.Gameschedule;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

/**
 * Created by owner on 2016-02-06.
 */
public interface GamescheduleMapper {
    @Select("SELECT * FROM gameschedule WHERE id = #{id}")
    Gameschedule getGameschedule(@Param("id") int gamescheduleId);

    @Select("SELECT COUNT(id) FROM gameschedule")
    int getLastId();
}