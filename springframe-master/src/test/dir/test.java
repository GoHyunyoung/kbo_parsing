import link.springapp.mvc.domain.Article;

import java.util.Map;
import java.util.TreeMap;

/**
 * Created by GoHyunyoung98 on 2016-07-25.
 */
public class test {
    public static void main(String[] args){
        Map<String,Object> articleMap=new TreeMap<>();
        for(int i=1;i<10;i++) {
            int article = i;
            articleMap.put(String.valueOf(i),article);
        }
        System.out.println(articleMap.get(String.valueOf(1)));
    }
}
