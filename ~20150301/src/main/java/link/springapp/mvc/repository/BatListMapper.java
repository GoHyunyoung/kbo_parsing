package link.springapp.mvc.repository;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Param;

/**
 * Created by owner on 2016-02-09.
 */

public interface BatListMapper {
    @Insert("INSERT INTO batList (bpList,team,name,tasu,anta,tajum,deukjum,tayul) "+
            "VALUES (#{bpList},#{team},#{name},#{tasu},#{anta},#{tajum},#{deukjum},#{tayul})")

    void setBatList(@Param("bpList") int bpList,
                    @Param("team") String team,
                    @Param("name") String name,
                    @Param("tasu") int tasu,
                    @Param("anta") int anta,
                    @Param("tajum") int tajum,
                    @Param("deukjum") int deukjum,
                    @Param("tayul") float tayul);
}