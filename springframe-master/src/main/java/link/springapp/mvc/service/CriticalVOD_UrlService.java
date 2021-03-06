package link.springapp.mvc.service;

import link.springapp.mvc.domain.CriticalVOD_Url;
import link.springapp.mvc.repository.CriticalVOD_UrlMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.ArrayList;

@Service
public class CriticalVOD_UrlService {
    @Autowired
    private CriticalVOD_UrlMapper criticalVOD_UrlMapper;

    public ArrayList<CriticalVOD_Url> getCriticalVOD_Url(int id) {
        ArrayList<CriticalVOD_Url> criticalVOD_Url = criticalVOD_UrlMapper.getCriticalVOD_Url(id);
        return criticalVOD_Url;
    }

    public int getCriticalVOD_UrlCount() {
        int count = criticalVOD_UrlMapper.getCriticalVOD_UrlCount();
        return count;
    }
}