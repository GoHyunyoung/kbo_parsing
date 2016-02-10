package link.springapp.mvc;

import link.springapp.mvc.domain.Gameinfo;
import link.springapp.mvc.service.GameinfoService;
import link.springapp.mvc.domain.Gameschedule;
import link.springapp.mvc.service.GamescheduleService;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.web.WebAppConfiguration;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.web.context.WebApplicationContext;

import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.List;

import static org.springframework.test.web.servlet.setup.MockMvcBuilders.webAppContextSetup;

/**
 * Created by owner on 2016-02-06.
 */

@RunWith(SpringJUnit4ClassRunner.class)
@WebAppConfiguration
@ContextConfiguration(
        {
                "file:src/main/webapp/WEB-INF/mvc-dispatcher-servlet.xml",
                "file:src/main/resources/spring.xml"
        }
)
public class Update_gameinfo {

    private MockMvc mockMvc;
    //  url에 들어가는 요소들
    private String url="";
    private String leagueId="";
    private String seriesId="";
    private String gameId="";
    private String gyear="";

    //    gameinfo에 넣을 데이터
    private String Ateam="";
    private String Hteam="";
    private String date="";
    private String str_time="";
    private String end_time="";
    private String stadium="";
    private int audience=0;
    private int[] Ainning=new int[12];
    private int[] Hinning=new int[12];
    private int[] ARHEB=new int[4];
    private int[] HRHEB=new int[4];
    private String finalhit="";
    private String homerun="";
    private String doru="";
    private String three_ruta="";
    private String byungsalta="";
    private String silcheck="";
    private int bpList=0;

    @Autowired
    private GamescheduleService gamescheduleService;
    @Autowired
    private GameinfoService gameinfoService;

    @SuppressWarnings("SpringJavaAutowiringInspection")
    @Autowired
    protected WebApplicationContext wac;

    @Before
    public void setup() {
        this.mockMvc = webAppContextSetup(this.wac).build();
    }

    //    url의 요소를 초기화
    public void url_init(){
        url="http://www.koreabaseball.com/Schedule/Game/BoxScore.aspx?";
        leagueId="leagueId=";
        seriesId="&seriesId=";
        gameId="&gameId=";
        gyear="&gyear=";
    }
    public void data_init(){
        Ateam="";
        Hteam="";
        date="";
        str_time="";
        end_time="";
        stadium="";
        audience=0;
        Ainning = new int[]{0,0,0,0,0,0,0,0,0,0,0,0};
        Hinning = new int[]{0,0,0,0,0,0,0,0,0,0,0,0};
        ARHEB= new int[]{0, 0, 0, 0};
        HRHEB= new int[]{0,0,0,0};
        finalhit="";
        homerun="";
        doru="";
        three_ruta="";
        byungsalta="";
        silcheck="";
    }
    public void setLeagueId(String leagueId) {
        this.leagueId += leagueId;
    }
    public void setSeriesId(String seriesId) {
        this.seriesId += seriesId;
    }
    public void setGameId(String gameId) {
        this.gameId += gameId;
    }
    public void setGyear(String gyear) {
        this.gyear += gyear;
    }

    public String getLeagueId() {
        return leagueId;
    }
    public String getSeriesId() {
        return seriesId;
    }
    public String getGameId() {
        return gameId;
    }
    public String getGyear() {
        return gyear;
    }

//    !!!!!!! 엑셀파일 등록시 주의사함!!!!!!!!!
//    Test 사용전 경기일정.xsl 파일을 조정
//    1. 경기가 없는 행은 삭제
//    2. 병합된 셀 삭제
//    3. 컬럼 이름 -> id/date/jamsil/mokdong/moonhak/suwon/daegu/gwangju/daejoen/sajik/masan
//    4. 날짜 확인
//    5. 데이터중에 null값 지양
//    6. 팀이름 수정(두산->OB
//    한화->HH
//    넥센->WO
//    삼성->SS
//    롯데->LT
//    NC->NC
//    SK->SK
//    LG->LG
//    KIA->HT
//    kt->kt )

    @Test
    public void mytest() {
//      URL Setting

//        DB에서 id=1부터 읽어옴
        int str_id=1;
//        마지막 id가 end_id
        int end_id=gamescheduleService.getLastId();

//            스케줄의 id=1인것부터 마지막까지 조회
        for(int id=str_id;id<=end_id;id++){

            Gameschedule gameschedule = gamescheduleService.getGameschedule(id);

//          1. gameschedule을 조회하여 잠실,목동,문학,수원,대구,광주,대전,사직,마산 에서 경기가 있었는지 확인
            String[] groundList={gameschedule.getJamsil(),
                    gameschedule.getMokdong(),
                    gameschedule.getMoonhak(),
                    gameschedule.getSuwon(),
                    gameschedule.getDaegu(),
                    gameschedule.getGwangju(),
                    gameschedule.getDaejeon(),
                    gameschedule.getSajik(),
                    gameschedule.getMasan()
            };


            List<String> playList = Arrays.asList(groundList);
            Iterator<String> iter_playList = playList.iterator();
            while(iter_playList.hasNext()) {

                url_init();
                data_init();

//              1. leagueId와 seriesId 설정
                setLeagueId("1");
                setSeriesId("0");

//              2. gyear과 gameId앞부분 설정
                setGyear(gameschedule.getDate().substring(0,4));
                String tmp_gameId=gameschedule.getDate().substring(0,4)+
                        gameschedule.getDate().substring(5,7)+
                        gameschedule.getDate().substring(8,10);

//                gameschedule 에서 null값이 있는 데이터는 skip
                try {
                    String play = iter_playList.next();
//              DB에 있는 경기의 내용이 공백이 아니면(NC-OB 이런식으로 경기가 있으면)
                    if (!play.isEmpty()) {
                        tmp_gameId += play.substring(0, 2) + play.substring(3, 5) + 0;
                        setGameId(tmp_gameId);
                        url += getLeagueId() + getSeriesId() + getGameId() + getGyear();

//                  URL설정완료
//                  JSoup을 이용한 파싱
                        try {
                            Document doc = Jsoup.connect(url).get();

//                        1. team 설정
                            Ateam = gameId.substring(16, 18);
                            Hteam = gameId.substring(18, 20);

//                        2. date 설정
                            date = gameId.substring(8, 16);

//                        div태그의 fightResult클래스의 자식태그인 p태그의 ballpark클래스
                            Element element = doc.select("div.fightResult p.ballpark").get(0);
//                      content는 HTML에서 p.ballpark를 파싱한 결과를 담는 String
//                        공백제거
                            String content = element.text().replaceAll(" ", "");

//                        System.out.println(content);

//                        3. playtime 설정
                            str_time = content.substring(content.indexOf("개시 :") + 5, content.indexOf("종료 :")).trim();
                            end_time = content.substring(content.indexOf("종료 :") + 5, content.indexOf("경기시간 :")).trim();

//                      !!! 만약 시작,종료시간이 없으면 일정에 있던 경기가 진행을 안한것이므로 DB에 넣으면안됨
                            if (str_time.isEmpty() || end_time.isEmpty())
                                continue;

//                        4. stadium 설정
                            stadium = content.substring(content.indexOf("구장 :") + 5, content.indexOf("관중 :")).trim();

//                        5. audience 설정
//                        숫자만 존재해야하므로 " "를 모두 ""로 변경
                            audience = Integer.valueOf(content.substring(content.indexOf("관중 :") + 5, content.indexOf("개시 :")).replaceAll(",", "").trim());

//                        6. inning 설정
                            for (int i = 0; i < 12; i++) {
//                            table태그의 socreBoard클래스의 자식태그인 td태그
                                if (doc.select("table.socreBoard tr:eq(0) td").get(i).text().equals("-"))
                                    Ainning[i] = 0;
                                else
                                    Ainning[i] = Integer.valueOf(doc.select("table.socreBoard tr:eq(0) td").get(i).text());
                                if (doc.select("table.socreBoard tr:eq(1) td").get(i).text().equals("-"))
                                    Hinning[i] = 0;
                                else
                                    Hinning[i] = Integer.valueOf(doc.select("table.socreBoard tr:eq(1) td").get(i).text());
                            }


//                        7. R,H,E,B 설정
//                        td 태그의 point 클래스
                            if (doc.select("table.socreBoard tr:eq(0) td.point").get(0).text().equals("-"))
                                ARHEB[0] = 0;
                            else
                                ARHEB[0] = Integer.valueOf(doc.select("table.socreBoard tr:eq(0) td.point").get(0).text());
                            if (doc.select("table.socreBoard tr:eq(1) td.point").get(0).text().equals("-"))
                                HRHEB[0] = 0;
                            else
                                HRHEB[0] = Integer.valueOf(doc.select("table.socreBoard tr:eq(1) td.point").get(0).text());

//                        td 태그의 hit 클래스
                            for (int i = 0; i < 3; i++) {
                                if (doc.select("table.socreBoard tr:eq(0) td.hit").get(i).text().equals("-"))
                                    ARHEB[i + 1] = 0;
                                else
                                    ARHEB[i + 1] = Integer.valueOf(doc.select("table.socreBoard tr:eq(0) td.hit").get(i).text());
                                if (doc.select("table.socreBoard tr:eq(1) td.hit").get(i).text().equals("-"))
                                    HRHEB[i + 1] = 0;
                                else
                                    HRHEB[i + 1] = Integer.valueOf(doc.select("table.socreBoard tr:eq(1) td.hit").get(i).text());
                            }

//                        결승타,홈런,도루,3루타,병살타,실책 설정

//                        8. 결승타 설정
//                        table태그의 tEx클래스의 '결승타'를 포함하는 tr태그의 직계자식 td태그
                            finalhit = doc.select("table.tEx tr:contains(결승타) > td").text();

//                        9. 홈런 설정
                            homerun = doc.select("table.tEx tr:contains(홈런) > td").text();

//                        10. 도루 설정
                            doru = doc.select("table.tEx tr:contains(도루) > td").text();

//                        11. 3루타 설정
                            three_ruta = doc.select("table.tEx tr:contains(3루타) > td").text();

//                        12. 병살타 설정
                            byungsalta = doc.select("table.tEx tr:contains(병살타) > td").text();

//                        13. 실책 설정
                            silcheck = doc.select("table.tEx tr:contains(실책) > td").text();

//                        14. 데이터 주입(DB에 주입)
//                        gameinfo 데이터를 DB에 주입
                            gameinfoService.setGameinfo(Ateam, Hteam,
                                    date, str_time, end_time, stadium, audience,
                                    Ainning, ARHEB, Hinning, HRHEB,
                                    finalhit, homerun, doru, three_ruta, byungsalta, silcheck, bpList);

//                        15. bpList 설정
                            bpList++;


//                        System.out.println(team);
//                        System.out.println(date);
//                        for(String str:playtime)
//                            System.out.print(str);
//                        System.out.println(stadium);
//                        System.out.println(audience);
//                        for(String str:inning)
//                            System.out.print(str);
//                        for(String str:RHEB)
//                            System.out.print(str);
//                        System.out.println(finalhit);
//                        System.out.println(homerun);
//                        System.out.println(doru);
//                        System.out.println(three_ruta);
//                        System.out.println(byungsalta);
//                        System.out.println(silcheck);
//                        System.out.println("---------------------");

                        } catch (IOException e) {
                            e.printStackTrace();
                        }

                    }
                }
                catch (NullPointerException e){
                    System.out.println(e.getMessage());
                    System.out.println(tmp_gameId+"에서 NullPointerException 발생");
                }
            }
        }
    }
}
