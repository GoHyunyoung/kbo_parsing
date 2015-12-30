package link.springapp.mvc.controller;

import link.springapp.mvc.service.UserService;
import link.springapp.mvc.domain.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
@Transactional
@RequestMapping("/")
public class HelloController {
	@Autowired
	private UserService userService;

	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String printWelcome(ModelMap model) {
		model.addAttribute("message", "Hello world!");
		return "hello";
	}

	@RequestMapping(value = "/userInfo", method = RequestMethod.GET)
	public String userInfo(ModelMap model, @RequestParam(value = "id", required = true) int userId) {
		User user = userService.getUser(userId);
		model.addAttribute("user", user);
		return "userInfo";
	}
}