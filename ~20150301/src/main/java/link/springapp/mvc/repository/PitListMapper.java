package link.springapp.mvc.repository;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Param;

/**
 * Created by owner on 2016-02-09.
 */

public interface PitListMapper {
    @Insert("INSERT INTO pitList (bpList,team,name,deungpan,inning,taja," +
            "toogusoo,tasoo,pianta,homerun,samjin,siljum,jacheck,avg_jacheck) "+

            "VALUES (#{bpList},#{team},#{name},#{deungpan},#{inning},#{taja}," +
            "#{toogusoo},#{tasoo},#{pianta},#{homerun},#{samjin},#{siljum},#{jacheck},#{avg_jacheck})")

    void setBatList(@Param("bpList") int bpList,
                    @Param("team") String team,
                    @Param("name") String name,
                    @Param("deungpan") String deungpan,
                    @Param("inning") String inning,
                    @Param("taja") int taja,
                    @Param("toogusoo") int toogusoo,
                    @Param("tasoo") int tasoo,
                    @Param("pianta") int pianta,
                    @Param("homerun") int homerun,
                    @Param("samjin") int samjin,
                    @Param("siljum") int siljum,
                    @Param("jacheck") int jacheck,
                    @Param("avg_jacheck") float avg_jacheck);
}