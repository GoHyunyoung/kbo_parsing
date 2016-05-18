package link.springapp.mvc.service;

import link.springapp.mvc.domain.Gameschedule;
import link.springapp.mvc.repository.GamescheduleMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

/**
 * Created by owner on 2016-02-06.
 */
@Service
public class GamescheduleService {
    @Autowired
    private GamescheduleMapper gamescheduleMapper;

    public Gameschedule getGameschedule(int id) {
        Gameschedule gameschedule = gamescheduleMapper.getGameschedule(id);
        return gameschedule;
    }

    //마지막 Id를 반환
    public int getLastId(){
        int LastId = gamescheduleMapper.getLastId();
        return LastId;
    }
}