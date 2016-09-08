package link.springapp.mvc.domain;

public class Article {
    private Integer id;
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

    public Integer getId() {
        return id;
    }
    public void setId(Integer id) {
        this.id = id;
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
    public void setConc(String main) {
        Conc = Conc;
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
    public String getawayT() {
        return awayT;
    }
    public void setawayT(String awayT) {
        this.awayT = awayT;
    }
    public String gethomeT() {return homeT;}
    public void sethomeT(String homeT) { this.homeT = homeT; }

    public Integer getA1() {return A1;}
    public void setA1(Integer A1) {this.A1 = A1;}
    public Integer getA2() {return A2;}
    public void setA2(Integer A2) {this.A2 = A2;}
    public Integer getA3() {return A3;}
    public void setA3(Integer A3) {this.A3 = A3;}
    public Integer getA4() {return A4;}
    public void setA4(Integer A4) {this.A4 = A4;}
    public Integer getA5() {return A5;}
    public void setA5(Integer A5) {this.A5 = A5;}
    public Integer getA6() {return A6;}
    public void setA6(Integer A6) {this.A6 = A6;}
    public Integer getA7() {return A7;}
    public void setA7(Integer A7) {this.A7 = A7;}
    public Integer getA8() {return A8;}
    public void setA8(Integer A8) {this.A8 = A8;}
    public Integer getA9() {return A9;}
    public void setA9(Integer A9) {this.A9 = A9;}
    public Integer getA10() {return A10;}
    public void setA10(Integer A10) {this.A10 = A10;}
    public Integer getA11() {return A11;}
    public void setA11(Integer A11) {this.A11 = A11;}
    public Integer getA12() {return A12;}
    public void setA12(Integer A12) {this.A12 = A12;}
    public Integer getAR() {return AR;}
    public void setAR(Integer AR) {this.AR = AR;}
    public Integer getAH() {return AH;}
    public void setAH(Integer AH) {this.AH = AH;}
    public Integer getAE() {return AE;}
    public void setAE(Integer AE) {this.AE = AE;}
    public Integer getAB() {return AB;}
    public void setAB(Integer AB) {this.AB = AB;}

    public Integer getH1() {return H1;}
    public void setH1(Integer H1) {this.H1 = H1;}
    public Integer getH2() {return H2;}
    public void setH2(Integer H2) {this.H2 = H2;}
    public Integer getH3() {return H3;}
    public void setH3(Integer H3) {this.H3 = H3;}
    public Integer getH4() {return H4;}
    public void setH4(Integer H4) {this.H4 = H4;}
    public Integer getH5() {return H5;}
    public void setH5(Integer H5) {this.H5 = H5;}
    public Integer getH6() {return H6;}
    public void setH6(Integer H6) {this.H6 = H6;}
    public Integer getH7() {return H7;}
    public void setH7(Integer H7) {this.H7 = H7;}
    public Integer getH8() {return H8;}
    public void setH8(Integer H8) {this.H8 = H8;}
    public Integer getH9() {return H9;}
    public void setH9(Integer H9) {this.H9 = H9;}
    public Integer getH10() {return H10;}
    public void setH10(Integer H10) {this.H10 = H10;}
    public Integer getH11() {return H11;}
    public void setH11(Integer H11) {this.H11 = H11;}
    public Integer getH12() {return H12;}
    public void setH12(Integer H12) {this.H12 = H12;}
    public Integer getHR() {return HR;}
    public void setHR(Integer HR) {this.HR = HR;}
    public Integer getHH() {return HH;}
    public void setHH(Integer HH) {this.HH = HH;}
    public Integer getHE() {return HE;}
    public void setHE(Integer HE) {this.HE = HE;}
    public Integer getHB() {return HB;}
    public void setHB(Integer HB) {this.HB = HB;}


    @Override
    public int hashCode() {
        final int prime = 31;
        int result = 1;
        result = prime * result + ((id == null) ? 0 : id.hashCode());
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
        if (id == null) {
            if (other.id != null)
                return false;
        } else if (!id.equals(other.id))
            return false;
        return true;
    }
}
