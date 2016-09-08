package link.springapp.mvc.domain;

/**
 * Created by moonlight on 2016. 9. 7..
 */
public class CriticalVOD_Url {
    private Integer id;
    private Integer Article_Id;
    private String vodUrl;

    public Integer getId() {
        return id;
    }
    public void setId(Integer id) {
        this.id = id;
    }
    public Integer getArticle_Id() {
        return Article_Id;
    }
    public void setArticle_Id(Integer Article_Id) {
        this.Article_Id = Article_Id;
    }
    public String getvodUrl() {
        return vodUrl;
    }
    public void setvodUrl(String vodUrl) {
        this.vodUrl = vodUrl;
    }
}
