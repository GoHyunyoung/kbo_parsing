package link.springapp.mvc.domain;

/**
 * Created by owner on 2016-02-10.
 */
public class PitList {

    private int id;
    private int bpList;
    private String team;
    private String name;
    private String deungpan;
    private String inning;
    private int taja;
    private int toogusoo;
    private int tasoo;
    private int pianta;
    private int homerun;
    private int samjin;
    private int siljum;
    private int jacheck;
    private float avg_jacheck;

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

    public String getDeungpan() {
        return deungpan;
    }

    public void setDeungpan(String deungpan) {
        this.deungpan = deungpan;
    }

    public String getInning() {
        return inning;
    }

    public void setInning(String inning) {
        this.inning = inning;
    }

    public int getTaja() {
        return taja;
    }

    public void setTaja(int taja) {
        this.taja = taja;
    }

    public int getToogusoo() {
        return toogusoo;
    }

    public void setToogusoo(int toogusoo) {
        this.toogusoo = toogusoo;
    }

    public int getTasoo() {
        return tasoo;
    }

    public void setTasoo(int tasoo) {
        this.tasoo = tasoo;
    }

    public int getPianta() {
        return pianta;
    }

    public void setPianta(int pianta) {
        this.pianta = pianta;
    }

    public int getHomerun() {
        return homerun;
    }

    public void setHomerun(int homerun) {
        this.homerun = homerun;
    }

    public int getSamjin() {
        return samjin;
    }

    public void setSamjin(int samjin) {
        this.samjin = samjin;
    }

    public int getSiljum() {
        return siljum;
    }

    public void setSiljum(int siljum) {
        this.siljum = siljum;
    }

    public int getJacheck() {
        return jacheck;
    }

    public void setJacheck(int jacheck) {
        this.jacheck = jacheck;
    }

    public float getAvg_jacheck() {
        return avg_jacheck;
    }

    public void setAvg_jacheck(float avg_jacheck) {
        this.avg_jacheck = avg_jacheck;
    }
}
