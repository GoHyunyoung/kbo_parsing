package link.springapp.mvc.controller;

import link.springapp.mvc.domain.Article;
import link.springapp.mvc.service.ArticleService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import java.util.Map;

@Controller
@Transactional
@RequestMapping("/")
public class HelloController {
	@Autowired
	private ArticleService articleService;

	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String printWelcome(ModelMap model) {
        Map<String,Object> articleMap;
	    for(int i=0;i<10;i++) {
            Article article = articleService.getArticle(i);
            model.addAllAttributes(articleMap,article);
        }
		return "hello";
	}

//	@RequestMapping(value = "/userInfo", method = RequestMethod.GET)
//	public String userInfo(ModelMap model, @RequestParam(value = "id", required = true) int userId) {
//		User user = userService.getUser(userId);
//		model.addAttribute("user", user);
//		return "userInfo";
//	}
}