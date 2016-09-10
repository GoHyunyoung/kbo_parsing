package link.springapp.mvc.domain;

/**
 * Created by moonlight on 2016. 9. 7..
 */
public class CriticalVOD_Url {
    private Integer Id;
    private Integer Article_Id;
    private String vodUrl;

    public Integer getId() {
        return Id;
    }

    public void setId(Integer id) {
        this.Id = id;
    }

    public Integer getArticle_Id() {
        return Article_Id;
    }

    public void setArticle_Id(Integer article_Id) {
        Article_Id = article_Id;
    }

    public String getVodUrl() {
        return vodUrl;
    }

    public void setVodUrl(String vodUrl) {
        this.vodUrl = vodUrl;
    }
}
