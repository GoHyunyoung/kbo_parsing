package link.springapp.mvc.service;

import link.springapp.mvc.domain.WinLosePitcher;
import link.springapp.mvc.repository.WinLosePitcherMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class WinLosePitcherService {
    @Autowired
    private WinLosePitcherMapper winlosePitcherMapper;

    public WinLosePitcher getWinlosePitcher(int id) {
        WinLosePitcher WinlosePitcher = winlosePitcherMapper.getWinlosePitcher(id);
        return WinlosePitcher;
    }
}