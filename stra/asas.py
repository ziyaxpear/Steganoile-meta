import streamlit as st
from PIL import Image

st.title("AKILLI TARIM UYGULAMLARI")
st.header("HOŞGELDİNİZ")
st.markdown("**AKILLI TARIM**")

st.write("Gelişen teknoloji hayatın her alanında olduğu gibi tarım sektöründe de yerini almış  ve almaya da hızla devam etmektedir. Artan nüfusa bağlı olarak oluşan talep karşısında tarımsal üretimde gelişme hızını ve verimi artırmak için tarımda teknoloji vazgeçilmez bir araç durumuna gelmiştir. İnternetin ise birçok alanda kullanılması ve aslında “nesnelerin interneti” ifadesi ile yaygınlaşması dördüncü sanayi devrimini oluşturmaya başlamıştır. Bu devrim Endüstri 4.0 devrimi olarak adlandırılmıştır. ")
image3 = Image.open('40.jpg')
st.image(image3, caption='Akıllı Tarım Uygulaması')

st.write("Tarım 1.0 şeklinde tanımlanan ilk devrimin yaşandığı zaman aralığının en temeldeki özelliği az oranda verimliliğin ve emeğin baskın olduğu üretim şeklinin hakim olmasıdır. 1950'lerin sonuna doğru sentetik pestisitler, gübreler ve daha büyük etkiler sağlayan makineler üretim maliyetlerini daha düşük düzeylere getirmiş ve bu sayede “Yeşil Devrim” denilen Tarım 2.0 zaman aralığı ortaya çıkmıştır. Düşük maliyetler ve yeni uygulamalarla birlikte tarımda verimlilik artışı yaşanmıştır. GPS sinyallerinin herkesin kullanımına açılmasıyla 1990'lı yıllarda Tarım 3.0 süreci, günümüzde daha çok “Hassas Tarım” kavramıyla birlikte isimlendirilmiştir. GPS teknolojisi ile birlikte manuel yönlendirme uygulamaları, hasat makinelerine uygulanan VRA (Variable Rate Application) sistemleriyle özellikle gübreleme sürecinin izlenmesi ve takibinin sağlanması bu dönemde uygulanmış belirgin teknoloji sistemler olarak ortaya çıkmıştır.")

image6 = Image.open('12.jpg')
st.image(image6, caption='Tarım 4.0')

st.write("2011 yılı sonrasında ilk defa Almanya'da Endüstri 4.0 ismiyle anılan, bilişim teknolojileri ile sanayinin birlikte çalışacağı üretimin entegre bilgisayar sistemleri ile maksimum verimle uygulanacağı ve yapay zekanın ön plana çıkacağı bir sanayi dönemecine girileceği açıklanmıştır. Endüstri 4.0 ile sanayide yaşanan devrimin benzer paralel bir süreçte tarım sektöründe yaşanmaya başlanmıştır.")
image2 = Image.open('tarim-blokchain.jpg')
st.image(image2, caption='Akıllı Tarım ve Yapay Zeka')

st.write("Geleneksel tarımın artan nüfusun ihtiyacını karşılamada yetersiz oluşu, tarımsal üretim kaynaklı çevre kirliliğinin artması, tarımsal sürdürülebilirliği sağlama zorunluluğu ve gıda güvenilirliği gibi ve diğer nedenler tarımsal üretimde yeni yaklaşımları gerekli kılmıştır. Bu nedenle yükselişte olan akıllı teknolojilerin tarımsal üretimde de kullanılması gündeme gelmiştir. Akıllı Tarım, tarımsal ürünlerin verimini ve kalitesini artırmak için modern teknolojiyi kullanan bir tarım yönetim kavramıdır. Özellikle bilgi ve sermaye, akıllı tarım teknolojileri için çok önemlidir. Akıllı tarım, felsefesi doğanın heterojenliğini yöneterek üretim yapmak olan, bilgi tabanlı tarımsal üretimdir.")
image5 = Image.open('5.jpg')
st.image(image5, caption='Geleneksel Tarım')

st.write("ABD'de çiftçilerin % 80'i akıllı tarım teknolojilerin kullanıyor iken, Avrupa'da bu oran yaklaşık %24 düzeyindedir. ABD pazarındaki güçlü büyüme, ABD'deki çiftçiler tarafından teknolojilerin benimsenme oranının yüksek olmasından kaynaklanmaktadır.")
image4 = Image.open('3.jpg')
st.image(image4, caption='Tarım 1.0')

st.write("Dünyada günden güne yaygınlaşan akıllı tarım uygulamaları Türkiye'de de uygulanmaya başlamış, ancak mevcut duruma bakıldığında istenilen ilerlemenin gerisinde kalındığı görülmüştür. Tarımsal üretim potansiyeli yüksek olan Türkiye'de bu potansiyelin doğru şekilde değerlendirilebilmesi için akıllı tarım teknolojilerinden faydalanılması gerekmektedir.Akıllı tarımla hayatımıza giren teknolojinin faydası kadar zararları da bulunmaktadır. Zararlarından kendimizi koruyup teknolojiden faydalanmak istiyoruz. Teknolojinin zararlarından bazıları bilgilerimizin çalınması, değiştirilmesi veya izinsiz kullanılmasıdır. Bu zararları minimuma indirmek için blokzincirinden faydalanılabilir.")
image1 = Image.open('t1.jpg')
st.image(image1, caption='Akıllı Tarım ve Blokzinciri')

st.write("Blokzinciri; güvenli bir şekilde paylaşılan, merkezi olmayan bir ana veri defteri olarak tanımlanır. Blokzinciri teknolojisi, toplu bir seçilmiş katılımcı grubunun verileri paylaşmasını sağlar. Blokzinciri, bulut servisleriyle birden fazla kaynaktan gelen işlem verileri kolayca toplanabilir, entegre edilebilir ve paylaşılabilir. Veriler, kriptografik karmalar biçiminde benzersiz tanımlayıcılarla birlikte zincirlenen paylaşılan bloklara bölünür. Blokzinciri, tek bir doğruluk kaynağıyla veri bütünlüğü sağlayarak veri çoğaltmasını ortadan kaldırır ve güvenliği artırır.")

st.write("Bir blokzinciri sisteminde dolandırıcılık ve veri müdahalesi önlenir çünkü veriler tarafların çoğunluğunun izni olmadan değiştirilemez. Blokzinciri kayıtları paylaşılabilir ama değiştirilemez. Biri verileri değiştirmeye çalışırsa, tüm katılımcılar uyarılır ve bu girişimi kimin yaptığını öğrenirler.")

st.write("Akıllı tarımla beraber hayatımıza giren teknolojinin blokzinciri yardımıyla zararlarından çok yararlı kısımları kullanılmak istenir. Bu amaçla geliştirilen projede blokzinciri, bilgilerimizin güvenilir, şeffaf, güncel ve izlenebilir olmasını sağlayacaktır. Uygulamanın kullanımı aşamasında sadece yetkili kişiler tarafından bilgiler değiştirilebilir olmasıyla proje güvenilir olacaktır. Ayrıca bilgilerin izin verilen kişiler tarafından güncel olarak görülebilmesiyle bilginin şeffaflığı ve izlenebilir olması sağlanacaktır.")

st.write("Bu çalışmada yapılmak istenen proje, dış etkilerden arındırılmış bir sera ortamında çalışacaktır. Ortamdaki ürünlerin çeşitliliğine bağlı olarak sera farklı bölümlere ayrılacaktır. Yetiştirilecek bitkilerin ideal ortamlarının oluşturulması için sıcaklık ve nem sensörleri gibi farklı sensörlerle veri toplanacaktır. Akıllı tarım denmesinin bir diğer sebebi olan ürünün durum değerlendirmesinde bulunmasıdır. Yani sensörlerden elde edilen değerlerin çiftlik sahibine, çiftlik çalışanlarına, toptancıya kısacası uygulamayı kullanan herkese ürün hakkında gerekli bilgilerin(ortamın sıcaklık, nem gibi ortam bilgilerinin yanında ürünün verim kalitesi) verilmeye çalışılacaktır. Ürün kalitesi değerlendirilme aşamasında bulanık mantıktan destek alınacaktır.")

st.write("     Bulanık Mantık kavramlarını yaşantımızın birçok yerinde görmekteyiz. Bu kavramlar yüksek, orta ve düşük değerlerdir. Bunun yanında; çok düşük, orta ve çok yüksek gibi ara değerleri de içerir. Bulanık Mantığın temelini bulanık küme oluşturmaktadır. Bulanık kümeler bulanık sistemlerin en temel konusudur. Klasik küme yaklaşımında elemanlar ya o kümeye aittir (1) ya da değildirler (0). Oysa Bulanık Mantık yaklaşımında ise elemanların o kümeye aitliği 0 ile 1 arasında değişir. Herhangi bir sıcaklık derecesi klasik kümeye göre ya sıcak olabilir ya da sıcak olmayabilir. Bulanık kümeye göre bu sıcaklık ait olduğu kümede belirli bir üyelik derecesine sahiptir. Örneğin; 5 ºС sıcaklık değeri çok düşük kümesine göre 0.5 üyelik derecesi ile düşük kümesi ise 0.667 üyelik derecesi ile ait olabilir.")

st.write("    Bu tez çalışmasında yetiştirilecek bitkilerin sıcaklık ve nem değerleri gibi farklı değişkenlerden elde edilen veriler bulanık mantık ile ürün kalitesi hakkında bize bilgi verecektir. Verilen bu bilgiler kullanıcıya blokzinciri yardımıyla güvenli hale getirilen bir web ara yüzü tasarlanacaktır. Tasarlanan bu ara yüz bitkinin anlık olarak sıcaklık, nem değerlerinin yanında ürün kalitesini de bildirecektir. Kullanıcılar bu verileri kullanarak üründeki verimin artması için tedbir alabilecektir. Bu şekilde, bitkiden en iyi verimle ürünler yetiştirilirken bilgiler şeffaf, güvenilir, güncel ve izlenebilir bir halde alacaktır.")


def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True

if check_password():
    st.write("Here goes your normal Streamlit app...")
    st.button("Click me")