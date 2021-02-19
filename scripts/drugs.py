import random
drugs = ["Acetaminophen","Adderall","Amitriptyline","Amlodipine","Amoxicillin","Ativan","Atorvastatin","Azithromycin","Benzonatate","Brilinta","Cephalexin","Ciprofloxacin","Citalopram","Clindamycin","Clonazepam","Cyclobenzaprine","Cymbalta","Doxycycline","Dupixent","Entresto","Entyvio","Farxiga","Gabapentin","Gilenya","Humira","Hydrochlorothiazide","Ibuprofen","Imbruvica","Invokana","Januvia","Jardiance","Kevzara","Lexapro","Lisinopril","Loratadine","Lyrica","Meloxicam","Metformin","Methadone","Metoprolol","Naproxen","Omeprazole","Onpattro","Otezla","Ozempic","Pantoprazole","Prednisone","Rybelsus","Tramadol","Trazodone","Viagra","Wellbutrin","Xanax", "Calcium carbonate","Captopril","Carafate","Carbamazepine","Carvedilol","Cefdinir","Ceftriaxone","Cefuroxime","Celebrex","Celecoxib","Celexa","Cephalexin","Cetirizine","Chantix","Chloroquine","Chlorthalidone","Cholecalciferol","Cialis","Cipro","Ciprofloxacin","Citalopram","Clarithromycin","Claritin","Clindamycin","Clonazepam","Clonidine","Clopidogrel","Clotrimazole","Clozapine","Codeine","Colace","Colchicine","Concerta","Coreg","Coumadin","Cozaar","Crestor","Cyanocobalamin","Cyclobenzaprine","Cymbalta","Haldol","Haloperidol","Harvoni","Heparin","Hepatitis B adult vaccine","Herceptin","Hizentra","Horizant","Humalog","HumaLOG KwikPen","Humira","Humulin 70/30","Humulin N","Humulin R","Hyaluronic Acid","Hycodan","Hydralazine","Hydrea","Hydrochlorothiazide","Hydrochlorothiazide and lisinopril","Hydrochlorothiazide and losartan","Hydrochlorothiazide and triamterene","Hydrochlorothiazide and valsartan","Hydrocodone","Hydrocodone and acetaminophen","Hydrocodone Bitartrate","Hydrocortisone","Hydrocortisone Cream","Hydrocortisone topical","Hydromorphone","Hydroxychloroquine","Hydroxyurea","Hydroxyzine","Hydroxyzine Hydrochloride","Hydroxyzine Pamoate","Hyoscyamine","Hysingla ER","Hytrin","Hyzaar", "Abilify","Acetaminophen","Aciphex","Actos","Acyclovir","Adderall","Advair Diskus","Advil","Albuterol","Albuterol Sulfate","Aldactone","Alendronate","Aleve","Alfuzosin","Allegra","Allopurinol","Alprazolam","Amantadine","Ambien","Amiodarone","Amitriptyline","Amlodipine","Amoxicillin","Amoxicillin and Clavulanate","Amphetamine and dextroamphetamine","Ampicillin","Anastrozole","Apixaban","Aricept","Aripiprazole","Aspirin","Atarax","Atenolol","Ativan","Atorvastatin","Atropine","Augmentin","Azathioprine","Azelastine","Azithromycin"]

def d(size):
    return "".join((str(random.randint(0,9)) for i in range(size)))

LOT = list(lambda x:+d(random.randint(6,9)), drugs)
dtype =["Preparations","Liquid","Tablet","Capsules","Suppositories","Drops","Inhalers","Injections","Implants","patches"]
comp = ["اروسازی تهران شیمی","داروسازی عبیدی","داروسازی رها","داروسازی سینا ژن","اکسیر گستر اسپادانا","داروسازی نانو حیات دارو","داروسازی رازک","داروسازی ایران دارو","داروسازی اکتوورکو","داروسازی راموفارمین","داروسازی زهراوی","دارو پخش  کارخانه","داروسازی امین","داروسازی اکسیر","داروسازی تهران دارو","داروسازی ابوریحان","داروسازی البرز دارو","داروسازی حکیم","داروسازی سبحان دارو","داروسازی باختر بیوشیمی","داروسازی جابربن حیان","داروسازی اسوه","داروسازی کیمیدارو","داروسازی تولید دارو","داروسازی گل دارو","داروسازی کاسپین تامین","داروسازی کیش مدیفارم","داروسازی پور سینا","داروسازی سینا دارو","داروسازی دانا","داروسازی لقمان","داروسازی شهر دارو","داروسازی فارابی","داروسازی سها","داروسازی روز دارو","داروسازی باریج اسانس","داروسازی درسا دارو","داروسازی الحاوی","داروسازی جالینوس","داروسازی ایران هورمون","داروسازی ایران ناژو","داروسازی پارس دارو","داروسازی خوارزمی","داروسازی ایران داروک","داروسازی بهوزان","داروسازی سامی ساز","داروسازی شفا","داروسازی آریا","داروسازی مهر دارو","داروسازی ثامن","داروسازی عماد درمان پارس","داروسازی آفا شیمی","داروسازی مینو","داروسازی شهید قاضی","داروسازی تسنیم","داروسازی دینه ایران(مجتمع صنایع)","داروسازی کوثر","داروسازی کوشان فارمد","داروسازی فارماشیمی","داروسازی تدبیر کالای جم","داروسازی سجاد داروی شرق","داروسازی بهسا","داروسازی آوه سینا","داروسازی زردبند","فرآورده های تزریقی دارویی ایران","داروسازی مداوا","مکمل های غذایی حیاتی کارن","داروسازی دنیای بهداشت","سونا طب پارسه","داروسازی سپیداج","داروسازی مینا","داروسازی ثنامد","داروسازی مرهم دارو","داروسازی گیاه اسانس","فن آوریهای نوین دارویی آتیه","دارو سازی طب مفید نیکان","صنعت دارویی شاری","داروسازی دارو درمان پارس","شرکت داروسازی قائم دارو","انستیتو پاستور كارخانه","داروسازی ایران آوند فر","لیوار","داروسازی پاک دارو","داروسازی اهورا دارو","داروسازی واریان فارمد","داروسازی سبحان انکولوژی","داروسازی روناک دارو","داروسازی گنجنه عصاره طبیعت","داروسازی سبز دارو اسپادانا","مجتمع کشت و صنعت میلاد خراسان","داروسازی فاتک شیمی پارس","داروسازی ژنیان فارمد","آتی فارمد","شرکت بین المللی سپید طب نیا","داروسازی پویش دارو","پودر شیر مشهد","نانو فناوران داروئی الوند","داروسازی نوتک فار","آرنا حیات دانش","بهشاد دارو","بنیان سلامت کسری","داروسازی ویستا تجارت پارس","داروسازی مهبان دارو","آرمان بهبود سینا","پگاه تهران","آرین سلامت سینا","سلامت گستر آرتیمان","نیک اختر آریا","پارس گیتا دارو","داروسازی زیست تخمیر","وانا دارو گستر","اکسون فارمد","دارویی و نهاده های زاگرس دارو پارسیان","داروسازی دلتا دارو","داروسازی فاخر","داروسازی فاران شیمی تویسرکان","داروسازی گیلارانکو","زیست دارو درمان پارس","دارو تدبیر پارس","اکسیر گل سرخ","شرکت تعاونی صنایع مکمل غذایی آریا بصیرت","رحمان گستران","داروسازی آریوژن فارمد","داروسازی بهستان تولید","داروسازی ساپونین ایران","داروسازی فرشته جویان","داروسازی ویتان فارمد","گلچای","گنجینه سلامت پاسارگاد","داروسازی نیاک","داروسازی ریحانه اصفهان","آوست دارو بهبود","نوآوران دارویی کیمیا","داروسازی آیدا شیمی توس","داروسازی خرمان","داروسازی رویان دارو","سیمرغ داروی عطار","هربی دارو","بهین تامین روزآمد","ایما ژن","دارو گستر مایسا","حکیم تجارت سهند","زیست دارو دانش","شرکت داروسازی گیاهی وشا دارو پارس (دانش بنیان)","داروسازی حنان بروجن","داروسازی دارو درمان سلفچگان","کوبل دارو","داروسازی حکیم مومن تیریزی","یاس دارو","هما فارمد","دارو سازی آرامیس فارمد","توسعه داروسازی دانش","داروسازی پارت كیمیا گرگان","داروسازی پژهان شیمی یزد","داروسازی دی دارو سلامت","داروسازی ندا","داروسازی رز فارمد","داروسازی شیراز سرم","کلین آسیا پارس","گیاه سبز زندگی","امید پارسینا دماوند","نانو دارو پؤوهان پردیس","اوکسین داروی وشت","هوگر دارو دانش","توسعه بازرگانی دارویی سبحان","ترانه های شفابخش طبیعت","ادیب اکسیر","داروسازی کیهان دارو","داروسازی آرام دارو گستر","اکسیر نانو سینا","داروسازی بارش طبیعت یاران","شرکت صنایع غذایی ایلیا پارس","ویتابیوتیکس تهران","گسترش میلاد فارمد","ابن ماسویه","داروسازی مرهم سازان سینا","شفا دارو آریا","کیمیاگر توس","سها جیسا","عرفان طب پارس","داروسازی رستاژن دارو","داروسازی سینا فراور","بهتا دارو آفرینش","Truevital","توسعه تجارت پرشین مهر","داروسازی ریحان نقش جهان","داروسازی آترا","داروسازی آسیا شیمی طب","داروسازی ایده گستر درمان","داروسازی بازرگانی پویش دارو","داروسازی توسعه آلفا","داروسازی درمان یاب دارو","داروسازی مرکز تحقیقات و توسعه شهید میثمی","آروین آرمان گستر","اکسیر مد پارس","بهارپایا","داروسازی زيست دارو درمان پارس","داروسازی دارو پژوهان لوتوس","داروسازی تهران نیل","دارو برگ شرق","فاروس فارمد","دارو سلامت فارمد","سلامت پرمون امین","سوباتان فارمد","تاکدشت","تک ژن زیست","پژوهشکده گیاهان دارویی","ایده آرای پیشگام","پرارین پارس","دانشگر زولنگ روسپینا","کی دارو فناوری سلامت","داروسازی دیموند","داروسازی بهنوار","داروسازی پارس سینا البرز","داروسازی دارلان دارو","داروسازی سلمی دارو","داروسازی کیمیا آفرینان البرز","داروسازی گاز بیهوشی شمال","داروسازی کیمیا آرا هرم","آریا تک خاور","داروسازی ماد","سلامت سازان پارسا","عسل داروی کیش","ویتا آریا","درمان گاز","داروسازی اکسیر دانش آسیا","داروسازی توسن دارو","داروسازی آراسته گستر پاسارگارد","داروسازی ایماژن","داروسازی بهار سبز طلایی","آسمان داروی پارس","فرنوش دارو طب","داروسازی آبادیس دارو پرگاس","آدونیس کیش","داروسازی آیلار طب آذر","دانا کسیان لرستان","قطره حیات","پایدار فردا","دارو مکمل آرین","سورن تک توس","تولید مواد اولیه داروپخش  تماد","داروسازی میم دارو","شیراز دارو حافظ","شهد آرا کاسپین","نوش دارو البرز","داروشفا طبیعی پدیده","ایمن طب دارو","نشاط داروی ساوه","آلماژن دارو","میم دارو","دارو پژوهان پاسارگاد","داروسازی پرشین پارس","یاس کویر میبد","کیمیا کالای رازی","صنایع غذایی دراژه","اصفهان شکلات","نوریا درمان پاسارگاد","نوشدارو دریا","نو آوری زیستی گویا","بهرسان فرتاک دارو","البرز فارمد","طبیعت زنده","مصون دارو","تک زیما دارو البرز","فن آوران روژان محقق دارو","نیتکا","وستاژن پارس","دارو درمان آرنگ","اکترو خاور میانه","آترا دارو صدر آزما","داروسازی دکتر رجبی","تحقیق و توسعه دایا دارو"]

def exp():
    return f"{random.randint(2018, 2035)}{pad(random.randint(1,12))}{pad(random.randint(1,28))}"

def pr():
    return int(random.random() * 100_000_000)

def sq():
    return random.randint(1, 50000)

c = random.choice
def drugs(i, j):
    return f"(N'{drug[i]}', {(j+1)+LOT[i]}, N'{c(dtype)}', N'{comp[j]}', N'{exp()}', {pr()}, {sq()})"

def get_drugs(i):
    manu = list(set([random.randint(0, len(comp)) for i in range(int(random.randint(1, len(comp))))]))
    return ",\n".join([drug(i,j) for j in manu])


print('INSERT INTO [dbo].[Drug] ([name],[batchNumber],[drugType],[manufacture],[ExpDate],[price],[stockQuantity])')
print('VALUES')

print(",\n".join((get_drugs(i) for i in range(len(drugs)))), end=";\n")