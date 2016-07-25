package link.springapp.mvc.controller;

import link.springapp.mvc.domain.Article;
import link.springapp.mvc.service.ArticleService;
import org.apache.ibatis.ognl.IntHashMap;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import java.util.HashMap;
import java.util.Map;
import java.util.TreeMap;

@Controller
@Transactional
@RequestMapping("/")
public class HelloController {
	@Autowired
	private ArticleService articleService;
	@RequestMapping(value = "/", method = RequestMethod.GET)
	public String printWelcome(ModelMap model) {
        HashMap<String,Object> articleMap=new HashMap<>();
	    for(int i=1;articleService.getArticle(i)!=null;i++) {
            Article article = articleService.getArticle(i);
            articleMap.put(String.valueOf(i),article);
        }
        model.addAttribute("articleMap",articleMap);
		return "hello";
	}

//	@RequestMapping(value = "/userInfo", method = RequestMethod.GET)
//	public String userInfo(ModelMap model, @RequestParam(value = "id", required = true) int userId) {
//		User user = userService.getUser(userId);
//		model.addAttribute("user", user);
//		return "userInfo";
//	}
}