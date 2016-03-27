package link.springapp.mvc;

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
import java.util.Iterator;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.view;
import static org.springframework.test.web.servlet.setup.MockMvcBuilders.webAppContextSetup;

@RunWith(SpringJUnit4ClassRunner.class)
@WebAppConfiguration
@ContextConfiguration(
        {
                "file:src/main/webapp/WEB-INF/mvc-dispatcher-servlet.xml",
                "file:src/main/resources/spring.xml"
        }
)
public class AppTests {
    private MockMvc mockMvc;

    @SuppressWarnings("SpringJavaAutowiringInspection")
    @Autowired
    protected WebApplicationContext wac;

    @Before
    public void setup() {
        this.mockMvc = webAppContextSetup(this.wac).build();
    }

    @Test
    public void simple() throws Exception {
        mockMvc.perform(get("/"))
                .andExpect(status().isOk())
                .andExpect(view().name("hello"));
    }

    @Test
    public void mytest() {
//        System.out.println("Hello world");
        try {
            Document doc = Jsoup.connect("http://www.koreabaseball.com/Schedule/Game/BoxScore.aspx?leagueId=1&seriesId=0&gameId=20150328NCOB0&gyear=2015").get();
            Iterator<Element> iterator = doc.select("table#xtable1").get(0).select("tbody tr").iterator();
//                    .select("table:eq(0)").iterator();
            while(iterator.hasNext())
                System.out.println(iterator.next());
//            String str = doc.select("table#xtable1 tbody tr:eq(0) th.name").toString();
//            str.toString();
        } catch (IOException e) {
            e.printStackTrace();
        }

    }
}
