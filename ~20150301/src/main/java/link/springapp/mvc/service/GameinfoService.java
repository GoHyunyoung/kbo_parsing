package link.springapp.mvc.service;

import link.springapp.mvc.domain.Gameinfo;
import link.springapp.mvc.repository.GameinfoMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * Created by owner on 2016-02-09.
 */

@Service
public class GameinfoService {
    @Autowired
    private GameinfoMapper gameinfoMapper;

    public void setGameinfo(String Ateam,String Hteam,
                            String date,
                            String str_time, String end_time,
                            String stadium,
                            int audience,
                            int[] Ainning,
                            int[] ARHEB,
                            int[] Hinning,
                            int[] HRHEB,
                            String finalhit,
                            String homerun,
                            String doru,
                            String three_ruta,
                            String byungsalta,
                            String silcheck,
                            int bpList) {

        gameinfoMapper.setGameinfo(Ateam,Hteam,
                date,
                str_time,end_time,
                stadium,
                audience,

                Ainning[0],
                Ainning[1],
                Ainning[2],
                Ainning[3],
                Ainning[4],
                Ainning[5],
                Ainning[6],
                Ainning[7],
                Ainning[8],
                Ainning[9],
                Ainning[10],
                Ainning[11],
                ARHEB[0],
                ARHEB[1],
                ARHEB[2],
                ARHEB[3],

                Hinning[0],
                Hinning[1],
                Hinning[2],
                Hinning[3],
                Hinning[4],
                Hinning[5],
                Hinning[6],
                Hinning[7],
                Hinning[8],
                Hinning[9],
                Hinning[10],
                Hinning[11],
                HRHEB[0],
                HRHEB[1],
                HRHEB[2],
                HRHEB[3],

                finalhit,
                homerun,
                doru,
                three_ruta,
                byungsalta,
                silcheck,
                bpList);
    }
}
