package link.springapp.mvc.repository;

import org.apache.ibatis.annotations.Insert;
import org.apache.ibatis.annotations.Param;

/**
 * Created by owner on 2016-02-09.
 */

public interface GameinfoMapper {
    @Insert("INSERT INTO gameinfo (Ateam,Hteam," +
            "date," +
            "str_time," + "end_time," +
            "stadium," +
            "audience," +
            "A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,AR,AH,AE,AB," +
            "H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,H11,H12,HR,HH,HE,HB," +
            "finalhit," +
            "homerun," +
            "doru," +
            "three_ruta," +
            "byungsalta," +
            "silcheck," +
            "bpList)\n" +

            "VALUES (#{Ateam},#{Hteam}," +
            "#{date}," +
            "#{str_time},#{end_time}," +
            "#{stadium}," +
            "#{audience}," +
            "#{A1},#{A2},#{A3},#{A4},#{A5},#{A6},#{A7},#{A8},#{A9},#{A10},#{A11},#{A12},#{AR},#{AH},#{AE},#{AB}," +
            "#{H1},#{H2},#{H3},#{H4},#{H5},#{H6},#{H7},#{H8},#{H9},#{H10},#{H11},#{H12},#{HR},#{HH},#{HE},#{HB}," +
            "#{finalhit}," +
            "#{homerun}," +
            "#{doru}," +
            "#{three_ruta}," +
            "#{byungsalta}," +
            "#{silcheck}," +
            "#{bpList})")

    void setGameinfo(@Param("Ateam") String Ateam,
                     @Param("Hteam") String Hteam,
                     @Param("date") String date,
                     @Param("str_time") String str_time,
                     @Param("end_time") String end_time,
                     @Param("stadium") String stadium,
                     @Param("audience") int audience,

                     @Param("A1") int A1,@Param("A2") int A2,@Param("A3") int A3,@Param("A4") int A4,@Param("A5") int A5,@Param("A6") int A6,
                     @Param("A7") int A7,@Param("A8") int A8,@Param("A9") int A9,@Param("A10") int A10,@Param("A11") int A11,@Param("A12") int A12,
                     @Param("AR") int AR,@Param("AH") int AH,@Param("AE") int AE,@Param("AB") int AB,
                     @Param("H1") int H1,@Param("H2") int H2,@Param("H3") int H3,@Param("H4") int H4,@Param("H5") int H5,@Param("H6") int H6,
                     @Param("H7") int H7,@Param("H8") int H8,@Param("H9") int H9,@Param("H10") int H10,@Param("H11") int H11,@Param("H12") int H12,
                     @Param("HR") int HR,@Param("HH") int HH,@Param("HE") int HE,@Param("HB") int HB,

                     @Param("finalhit") String finalhit,
                     @Param("homerun") String homerun,
                     @Param("doru") String doru,
                     @Param("three_ruta") String three_ruta,
                     @Param("byungsalta") String byungsalta,
                     @Param("silcheck") String silcheck,
                     @Param("bpList") int bpList);
}