package link.springapp.mvc.service;

import link.springapp.mvc.repository.BatListMapper;
import link.springapp.mvc.repository.PitListMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * Created by owner on 2016-02-09.
 */

@Service
public class PitListService {
    @Autowired
    private PitListMapper pitListMapper;

    public void setPitList(int bpList,String team,String name,String deungpan,String inning,
                           int taja,int toogusoo,int tasoo,int pianta,int homerun,
                           int samjin,int siljum,int jacheck,float avg_jacheck){

        pitListMapper.setBatList(bpList, team, name, deungpan, inning, taja,toogusoo,
                tasoo, pianta, homerun, samjin, siljum, jacheck, avg_jacheck);
    }
}
