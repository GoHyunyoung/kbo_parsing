package link.springapp.mvc.domain;

/**
 * Created by moonlight on 2016. 9. 6..
 */
public class winlosePitcher {
    private Integer id;
    private Integer Article_Id;
    private String winPlayerName;
    private Integer winPlayerWinCount;
    private Integer winPlayerLoseCount;
    private Double winPlayerERA;
    private String winPlayerFaceUrl;
    private String losePlayerName;
    private Integer losePlayerWinCount;
    private Integer losePlayerLoseCount;
    private Double losePlayerERA;
    private String losePlayerFaceUrl;

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
    public String getWinPlayerName() {return winPlayerName;}
    public void setWinPlayerName(String winPlayerName) {this.winPlayerName = winPlayerName;}
    public Integer getWinPlayerWinCount() {return winPlayerWinCount;}
    public void setWinPlayerWinCount(Integer winPlayerWinCount) {this.winPlayerWinCount = winPlayerWinCount;}
    public Integer getWinPlayerLoseCount() {return winPlayerLoseCount;}
    public void setWinPlayerLoseCount(Integer winPlayerLoseCount) {this.winPlayerLoseCount = winPlayerLoseCount;}
    public Double getWinPlayerERA() {return winPlayerERA;}
    public void setWinPlayerERA(Double winPlayerERA) {this.winPlayerERA = winPlayerERA;}
    public String getWinPlayerFaceUrl() {return winPlayerFaceUrl;}
    public void setWinPlayerFaceUrl(String winPlayerFaceUrl) {this.winPlayerFaceUrl = winPlayerFaceUrl;}
    public String getLosePlayerName() {return losePlayerName;}
    public void setLosePlayerName(String losePlayerName) {this.losePlayerName = losePlayerName;}
    public Integer getLosePlayerWinCount() {return losePlayerWinCount;}
    public void setLosePlayerWinCount(Integer losePlayerWinCount) {this.losePlayerWinCount = losePlayerWinCount;}
    public Integer getLosePlayerLoseCount() {return losePlayerLoseCount;}
    public void setLosePlayerLoseCount(Integer losePlayerLoseCount) {this.losePlayerLoseCount = losePlayerLoseCount;}
    public Double getLosePlayerERA() {return losePlayerERA;}
    public void setLosePlayerERA(Double losePlayerERA) {this.losePlayerERA = losePlayerERA;}
    public String getLosePlayerFaceUrl() {return losePlayerFaceUrl;}
    public void setLosePlayerFaceUrl(String losePlayerFaceUrl) {this.losePlayerFaceUrl = losePlayerFaceUrl;}
}
