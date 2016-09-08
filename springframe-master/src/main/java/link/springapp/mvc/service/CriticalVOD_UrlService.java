package link.springapp.mvc.service;

import link.springapp.mvc.domain.CriticalVOD_Url;
import link.springapp.mvc.repository.CriticalVOD_UrlMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CriticalVOD_UrlService {
    @Autowired
    private CriticalVOD_UrlMapper CriticalVOD_UrlMapper;

    public CriticalVOD_Url[] getCriticalVOD_Url(int id) {
        CriticalVOD_Url[] CriticalVOD_Url = CriticalVOD_UrlMapper.getCriticalVOD_Url(id);
        return CriticalVOD_Url;
    }

    public int getCriticalVOD_UrlCount() {
        int count = CriticalVOD_UrlMapper.getCriticalVOD_UrlCount();
        return count;
    }
}