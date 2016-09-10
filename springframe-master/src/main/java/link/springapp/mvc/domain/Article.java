package link.springapp.mvc.domain;

public class Article {
    private Integer Id;
    private String date;
    private String Head;
    private String Intro;
    private String Main;
    private String Conc;
    private String Url;
    private String emblem;
    private String awayT;
    private String homeT;
    private Integer A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,A11,A12,AR,AH,AE,AB;
    private Integer H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,H11,H12,HR,HH,HE,HB;



    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((Id == null) ? 0 : Id.hashCode());
        return result;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Article other = (Article) obj;
        if (Id == null) {
            if (other.Id != null)
                return false;
        } else if (!Id.equals(other.Id))
            return false;
        return true;
    }

    public Integer getId() {
        return Id;
    }

    public void setId(Integer id) {
        this.Id = id;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getHead() {
        return Head;
    }

    public void setHead(String head) {
        Head = head;
    }

    public String getIntro() {
        return Intro;
    }

    public void setIntro(String intro) {
        Intro = intro;
    }

    public String getMain() {
        return Main;
    }

    public void setMain(String main) {
        Main = main;
    }

    public String getConc() {
        return Conc;
    }

    public void setConc(String conc) {
        Conc = conc;
    }

    public String getUrl() {
        return Url;
    }

    public void setUrl(String url) {
        Url = url;
    }

    public String getEmblem() {
        return emblem;
    }

    public void setEmblem(String emblem) {
        this.emblem = emblem;
    }

    public String getAwayT() {
        return awayT;
    }

    public void setAwayT(String awayT) {
        this.awayT = awayT;
    }

    public String getHomeT() {
        return homeT;
    }

    public void setHomeT(String homeT) {
        this.homeT = homeT;
    }

    public Integer getA1() {
        return A1;
    }

    public void setA1(Integer a1) {
        A1 = a1;
    }

    public Integer getA2() {
        return A2;
    }

    public void setA2(Integer a2) {
        A2 = a2;
    }

    public Integer getA3() {
        return A3;
    }

    public void setA3(Integer a3) {
        A3 = a3;
    }

    public Integer getA4() {
        return A4;
    }

    public void setA4(Integer a4) {
        A4 = a4;
    }

    public Integer getA5() {
        return A5;
    }

    public void setA5(Integer a5) {
        A5 = a5;
    }

    public Integer getA6() {
        return A6;
    }

    public void setA6(Integer a6) {
        A6 = a6;
    }

    public Integer getA7() {
        return A7;
    }

    public void setA7(Integer a7) {
        A7 = a7;
    }

    public Integer getA8() {
        return A8;
    }

    public void setA8(Integer a8) {
        A8 = a8;
    }

    public Integer getA9() {
        return A9;
    }

    public void setA9(Integer a9) {
        A9 = a9;
    }

    public Integer getA10() {
        return A10;
    }

    public void setA10(Integer a10) {
        A10 = a10;
    }

    public Integer getA11() {
        return A11;
    }

    public void setA11(Integer a11) {
        A11 = a11;
    }

    public Integer getA12() {
        return A12;
    }

    public void setA12(Integer a12) {
        A12 = a12;
    }

    public Integer getAR() {
        return AR;
    }

    public void setAR(Integer AR) {
        this.AR = AR;
    }

    public Integer getAH() {
        return AH;
    }

    public void setAH(Integer AH) {
        this.AH = AH;
    }

    public Integer getAE() {
        return AE;
    }

    public void setAE(Integer AE) {
        this.AE = AE;
    }

    public Integer getAB() {
        return AB;
    }

    public void setAB(Integer AB) {
        this.AB = AB;
    }

    public Integer getH1() {
        return H1;
    }

    public void setH1(Integer h1) {
        H1 = h1;
    }

    public Integer getH2() {
        return H2;
    }

    public void setH2(Integer h2) {
        H2 = h2;
    }

    public Integer getH3() {
        return H3;
    }

    public void setH3(Integer h3) {
        H3 = h3;
    }

    public Integer getH4() {
        return H4;
    }

    public void setH4(Integer h4) {
        H4 = h4;
    }

    public Integer getH5() {
        return H5;
    }

    public void setH5(Integer h5) {
        H5 = h5;
    }

    public Integer getH6() {
        return H6;
    }

    public void setH6(Integer h6) {
        H6 = h6;
    }

    public Integer getH7() {
        return H7;
    }

    public void setH7(Integer h7) {
        H7 = h7;
    }

    public Integer getH8() {
        return H8;
    }

    public void setH8(Integer h8) {
        H8 = h8;
    }

    public Integer getH9() {
        return H9;
    }

    public void setH9(Integer h9) {
        H9 = h9;
    }

    public Integer getH10() {
        return H10;
    }

    public void setH10(Integer h10) {
        H10 = h10;
    }

    public Integer getH11() {
        return H11;
    }

    public void setH11(Integer h11) {
        H11 = h11;
    }

    public Integer getH12() {
        return H12;
    }

    public void setH12(Integer h12) {
        H12 = h12;
    }

    public Integer getHR() {
        return HR;
    }

    public void setHR(Integer HR) {
        this.HR = HR;
    }

    public Integer getHH() {
        return HH;
    }

    public void setHH(Integer HH) {
        this.HH = HH;
    }

    public Integer getHE() {
        return HE;
    }

    public void setHE(Integer HE) {
        this.HE = HE;
    }

    public Integer getHB() {
        return HB;
    }

    public void setHB(Integer HB) {
        this.HB = HB;
    }
}
