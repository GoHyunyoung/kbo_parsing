package link.springapp.mvc.service;

import link.springapp.mvc.repository.BatListMapper;
import link.springapp.mvc.repository.GameinfoMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * Created by owner on 2016-02-09.
 */

@Service
public class BatListService {
    @Autowired
    private BatListMapper batListMapper;

    public void setBatList(int bpList,String team,String name,int tasu,
                           int anta,int tajum, int deukjum, float tayul) {

        batListMapper.setBatList(bpList,team,name,tasu,anta,tajum,deukjum,tayul);
    }
}
