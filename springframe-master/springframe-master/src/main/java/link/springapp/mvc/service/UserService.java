package link.springapp.mvc.service;

import link.springapp.mvc.domain.User;
import link.springapp.mvc.repository.UsersMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserService {
    @Autowired
    private UsersMapper usersMapper;

    public User getUser(int id) {
        User user = usersMapper.getUser(id);
        return user;
    }
}