package link.springapp.mvc;

import link.springapp.mvc.domain.Gameschedule;
import link.springapp.mvc.service.GamescheduleService;
import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.test.context.ContextConfiguration;
import org.springframework.test.context.junit4.SpringJUnit4ClassRunner;
import org.springframework.test.context.web.WebAppConfiguration;
import org.springframework.test.web.servlet.MockMvc;
import org.springframework.web.context.WebApplicationContext;

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
    //    url에 들어가는 요소들
    private String url="";
    private String leagueId="";
    private String seriesId="";
    private String gameId="";
    private String gyear="";


    @Autowired
    private GamescheduleService gamescheduleService;

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

    @Test
    public void mytest() {
//        DB에서 id=1부터 읽어옴
        int str_id=1;
//        마지막 id가 end_id
        int end_id=gamescheduleService.getLastId();

//            id=1인것부터 마지막까지 조회
        for(int id=str_id;id<=end_id;id++){

            Gameschedule gameschedule = gamescheduleService.getGameschedule(id);

//          3. 잠실,목동,문학,수원,대구,광주,대전,사직,마산 에서 경기가 있었는지 확인
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

//              1. leagueId와 seriesId 설정
                setLeagueId("1");
                setSeriesId("0");

//              2. gyear과 gameId앞부분 설정
                setGyear(gameschedule.getDate().substring(0,4));
                String tmp_gameId=gameschedule.getDate().substring(0,4)+
                        gameschedule.getDate().substring(5,7)+
                        gameschedule.getDate().substring(8,10);


                String play = iter_playList.next();
//              DB에 있는 경기의 내용이 공백이 아니면(NC-OB 이런식으로 경기가 있으면)
                if (play != "") {
                    tmp_gameId += play.substring(0, 2) + play.substring(3, 5) + 0;
                    setGameId(tmp_gameId);
                    url += getLeagueId() + getSeriesId() + getGameId() + getGyear();
                    System.out.println("url -> "+url);
                }
            }
        }
    }
}
