package link.springapp.mvc.domain;

/**
 * Created by owner on 2016-02-10.
 */
public class BatList {
    private int id;
    private int bpList;


    private String team;
    private String name;
    private String tasu;
    private String anta;
    private String tajum;
    private String deukjum;
    private String tayul;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getTeam() {
        return team;
    }

    public int getBpList() {
        return bpList;
    }

    public void setBpList(int bpList) {
        this.bpList = bpList;
    }

    public void setTeam(String team) {
        this.team = team;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getTasu() {
        return tasu;
    }

    public void setTasu(String tasu) {
        this.tasu = tasu;
    }

    public String getAnta() {
        return anta;
    }

    public void setAnta(String anta) {
        this.anta = anta;
    }

    public String getTajum() {
        return tajum;
    }

    public void setTajum(String tajum) {
        this.tajum = tajum;
    }

    public String getDeukjum() {
        return deukjum;
    }

    public void setDeukjum(String deukjum) {
        this.deukjum = deukjum;
    }

    public String getTayul() {
        return tayul;
    }

    public void setTayul(String tayul) {
        this.tayul = tayul;
    }
}
