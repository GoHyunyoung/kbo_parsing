package link.springapp.mvc.service;

import link.springapp.mvc.domain.winlosePitcher;
import link.springapp.mvc.repository.winlosePitcherMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class winlosePitcherService {
    @Autowired
    private winlosePitcherMapper WinlosePitcherMapper;

    public winlosePitcher getWinlosePitcher(int id) {
        winlosePitcher WinlosePitcher = WinlosePitcherMapper.getWinlosePitcher(id);
        return WinlosePitcher;
    }
}