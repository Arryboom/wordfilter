from django.http import JsonResponse
import jieba

# Create your views here.

dict = {
    "无修正": "",
    "被插": "", "裸舞视": "", "春药": "", "秘唇": "", "爱液": "", "乳头": "", "娘西皮": "", "骚水": "", "色情小说": "", "鸡奸": "",
    "迷昏药": "", "狗日的": "", "阴核": "", "拳交": "", "铃声": "", "穴口": "", "妓女": "", "狂操": "", "全家不得好死": "", "人兽": "",
    "裹本": "", "援交": "", "h动漫": "", "干穴": "", "成人卡通": "", "中年美妇": "", "爆乳": "", "寂寞男": "", "狂插": "", "杨思敏": "",
    "阴茎": "", "porn": "", "18禁": "", "麻醉药": "", "阴阜": "", "淫威": "", "我草": "", "屄": "", "草你丫": "", "伦理大": "",
    "肉棍": "", "死全家": "", "淫騷妹": "", "母奸": "", "人渣": "", "抽插": "", "迷昏口": "", "肛门": "", "骚嘴": "", "卧艹": "",
    "菊门": "", "舔阴": "", "少妇": "", "性交图片": "", "要射了": "", "兽交": "", "色情服务": "", "你麻痹": "", "暴乳": "", "淫叫": "",
    "阴唇": "", "狗娘养": "", "马勒": "", "玉乳": "", "成人网站": "", "淫糜": "", "内裤": "", "乖乖粉": "", "性奴集中营": "", "成人游戏": "",
    "性虎": "", "操烂": "", "群交": "", "兽奸": "", "浪妇": "", "口活": "", "狼友": "", "杀b": "", "肉逼": "", "猛男": "",
    "夏川纯": "", "干你娘": "", "a片": "", "迷奸粉": "", "鸡吧": "", "色欲": "", "巨奶": "", "做爱": "", "成人色情": "", "强暴": "",
    "肉茎": "", "色情电影": "", "摇头丸": "", "我就色": "", "性感诱惑": "", "操你全家": "", "大波": "", "风月大陆": "", "密穴": "", "爆你菊": "",
    "美乳": "", "精液": "", "操他妈": "", "高潮": "", "作爱": "", "迷藥": "", "迷情水": "", "拔出来": "", "屁眼": "", "谜奸药": "",
    "贱比": "", "狗杂种": "", "色诱": "", "sb": "", "骚货": "", "插暴": "", "豪乳": "", "欠干": "", "美艳少妇": "", "cao你": "",
    "射颜": "", "幼交": "", "暴淫": "", "漏乳": "", "摸奶": "", "成人文学": "", "骚妇": "", "迷魂藥": "", "一丝不挂": "", "情趣用品": "",
    "色逼": "", "玉穴": "", "快感": "", "擦你妈": "", "淫魔": "", "成人视": "", "阴毛": "", "真他妈": "", "你吗b": "", "肉唇": "",
    "阴间来电": "", "呻吟": "", "美女裸体": "", "美穴": "", "小xue": "", "刹笔": "", "淫虫": "", "咪咪": "", "激情": "", "色b": "",
    "贱b": "", "阴b": "", "incest": "", "学生妹": "", "淫兽": "", "胸推": "", "成人论坛": "", "我日你": "", "大力抽送": "", "阴茎助勃": "",
    "淫亵": "", "玉女心经": "", "sexinsex": "", "写真": "", "淫水": "", "a4u": "", "凌辱": "", "secom": "", "铃木麻": "", "美腿": "",
    "全家死光": "", "轮暴": "", "少修正": "", "肏死": "", "射爽": "", "你他妈": "", "迷奸": "", "下贱": "", "兽欲": "", "汤加丽": "",
    "脱内裤": "", "龟头": "", "轮操": "", "迷奸药": "", "花花公子": "", "火辣": "", "艳情小说": "", "菊花洞": "", "操你妈": "", "内射": "",
    "发情": "", "爆草": "", "日逼": "", "干你妈": "", "裸露": "", "amateur": "", "屌": "", "干死你": "", "淫荡": "", "奶子": "",
    "乳交": "", "叫床": "", "情色": "", "淫兽学": "", "g片": "", "精子": "", "颜射": "", "操死": "", "色情片": "", "淫虐": "",
    "射精": "", "淫荡视频": "", "嫩女": "", "我干": "", "熟妇": "", "粉穴": "", "淫娃": "", "我操": "", "骚比": "", "fuck": "",
    "肉棒": "", "99bb": "", "操黑": "", "阳具": "", "淫浪": "", "裸聊": "", "原味内衣": "", "乳沟": "", "成人图": "", "伦理电影": "",
    "逼奸": "", "骚女": "", "性感妖娆": "", "anal": "", "阉割": "", "阴茎增大": "", "和弦": "", "强jian": "", "阴精": "", "草你吗": "",
    "乱交": "", "成人片": "", "口射": "", "金鳞岂是池中物": "", "别他吗": "", "贱货": "", "色情影片": "", "小逼": "", "换妻俱乐部": "", "色猫": "",
    "色电影": "", "聊性": "", "婊子": "", "品香堂": "", "成人小": "", "诱奸": "", "喷精": "", "自慰": "", "迷昏藥": "", "巨乳": "",
    "插b": "", "吃精": "", "蜜液": "", "一夜欢": "", "淫液": "", "裸聊网": "", "就去日": "", "无耻": "", "色情图片": "", "裙中性运动": "",
    "集体淫": "", "乱奸": "", "色妹妹": "", "迷情粉": "", "招妓": "", "发浪": "", "迷幻藥": "", "仓井空": "", "色情表演": "", "男公关": "",
    "插逼": "", "食精": "", "乳爆": "", "买春": "", "迷魂香": "", "国产av": "", "女优": "", "浑圆": "", "狗操": "", "口爆": "",
    "无码": "", "寂寞女": "", "陰唇": "", "校鸡": "", "插比": "", "g点": "", "成人小说": "", "干你": "", "淫电影": "", "欲仙欲死": "",
    "幼男": "", "xing伴侣": "", "释欲": "", "成人聊": "", "推油": "", "淫河": "", "xiao77": "", "性交": "", "乳房": "", "被干": "",
    "扌由插": "", "盗撮": "", "浪叫": "", "淫书": "", "色小说": "", "性虐": "", "奈美": "", "亚情": "", "捏弄": "", "口淫": "",
    "偷欢": "", "鸡巴": "", "玉蒲团": "", "夜勤病栋": "", "风骚": "", "色视频": "", "淫妻": "", "装b": "", "迷魂药": "", "露b": "",
    "性饥渴": "", "发生关系": "", "sm": "", "粉嫩": "", "操逼": "", "开苞": "", "黑逼": "", "精神药品": "", "性奴": "", "裸体写真": "",
    "卧槽": "", "艹你": "", "成人电": "", "文做": "", "嫩逼": "", "强奸处女": "", "淫媚": "", "煞逼": "", "摸胸": "", "体奸": "",
    "包二奶": "", "丝诱": "", "招鸡": "", "插我": "", "砲友": "", "嫩穴": "", "暴干": "", "沙比": "", "成人dv": "", "伦理片": "",
    "脱光": "", "淫妇": "", "骚逼": "", "熟母": "", "narcotic": "", "混蛋": "", "张筱雨": "", "性爱": "", "肉欲": "", "处男": "",
    "爽死我了": "", "贱人": "", "好嫩": "", "前凸后翘": "", "淫荡美女": "", "淫情": "", "乱伦类": "", "性伙伴": "", "暴奸": "", "男奴": "",
    "裸陪": "", "阴道": "", "一本道": "", "多人轮": "", "插你": "", "日烂": "", "骚穴": "", "陰戶": "", "体位": "", "限量": "",
    "全裸": "", "淫样": "", "一ye情": "", "性福情": "", "调教": "", "妹上门": "", "傻b": "", "性交视频": "", "舞女": "", "adult": "",
    "淫声浪语": "", "性技巧": "", "色情网站": "", "浪女": "", "肥逼": "", "少年阿宾": "", "轮奸": "", "h动画": "", "三级片": "", "肏你": "",
    "色盟": "", "不穿": "", "淫色": "", "黄片": "", "赤裸": "", "干死": "", "口交": "", "sm女王": "", "媚外": "", "按摩": "",
    "成人文": "", "套弄": "", "人妻": "", "淫情女": "", "淫靡": "", "潮吹": "", "兽性": "", "色界": "", "淫魔舞": "", "妈了个逼": "",
    "大sb": "", "一夜情": "", "大乳": "", "操你大爷": "", "偷拍": "", "淫教师": "", "炮友": "", "双臀": "", "抓胸": "", "强奸": "",
    "舔脚": "", "巨屌": "", "欲火": "", "成人电影": "", "几吧": "", "操你祖宗": "", "脚交": "", "白嫩": "", "日你妈": "", "抽一插": "",
    "封面女郎": "", "松岛枫": "", "肉洞": "", "淫兽学园": "", "流淫": "", "阴户": "", "荡妇": "", "乱伦": "", "操我": "", "美幼": "",
    "刺激": "", "肉具": "", "yin荡": "", "爽片": "", "淫穴": "", "迷幻药": "", "肉缝": "", "肛交": "", "性伴侣": "", "小穴": "",
    "淫术炼金士": "", "插进": "", "性欲": "", "性感少": "", "淫荡照片": "", "a4y": "", "自拍": "", "乱伦小": "", "裤袜": "", "淫照": "",
    "应召": "", "gay片": "", "金麟岂是池中物": "", "妈逼": "", "hardcore": "", "兼职": "", "屁股": "", "傻比": "", "妹按摩": "", "美女写真": "",
    "美少妇": "", "后庭": "", "婊子养的": "", "性息": "", "麻痹的": "", "morphine": "", "美逼": "", "熟女": "", "穴图": "", "手淫": "",
    "淫母": "", "裸照": "", "后穴": "", "援助交际": "", "丝袜": "", "淫女": "", "死逼": "", "性服务": "", "揉乳": "", "幼女": "",
    "按摩棒": "", "虎骑": "", "淫贱": "", "浪逼": "", "放尿": "", "欲女": "", "酥痒": "", "骚浪": "", "荡女": "", "被操": "",
    "肉穴": "", "菊穴": "", "狗草": "", "陰道": "", "你妈的": "", "全家死绝": "", "阴蒂": "", "淫乱": "", "吸精": "", "色区": "",
    "相奸": "", "迷情药": "", "插阴": "", "煞笔": "", "白痴": "", "下体": "", "阴部": "", "傻逼": "", "蜜穴": "", "潮喷": "",
    "厕奴": "", "淫肉": "", "奸情": "", "爱女人": "", "tokyohot": "", "伦理毛": "", "操你娘": "", "惹火身材": "", "色色": "", "迷药": "",
    "美女上门": "", "亚砷酸钾": "", "九ping": "", "售健卫": "", "电话监": "", "diacetylmorphine": "", "falungong": "", "爱他死": "",
    "麻古": "", "电狗": "",
    "雄烯二醇": "", "亚硝酰乙氧": "", "普萘洛尔": "", "美沙酮": "", "售单管": "", "自sha": "", "电话拦截器": "", "胰岛素样生长因子": "", "亚砷酸钠": "",
    "推背图": "",
    "法lg": "", "法o功": "", "jiuping": "", "售防身": "", "自fen": "", "甲基安非他明": "", "售步枪": "", "咖啡因": "", "人类灭亡进程表": "",
    "erythropoietin": "",
    "杜冷丁": "", "电警棒": "", "三去车仑": "", "真善忍": "", "麻黄草": "", "明慧网": "", "heroin": "", "售纯度": "", "促红细胞生成素": "",
    "根达亚文明": "",
    "售枪支": "", "统一教": "", "诸世纪": "", "枪决女犯": "", "benzodiazepines": "", "售氯胺": "", "伪火": "", "枪模": "", "tamoxifen": "",
    "氧化铊": "",
    "亚硒酸氢钠": "", "福音会": "", "中国教徒": "", "苯巴比妥": "", "售子弹": "", "电击枪": "", "大法弟子": "", "清海无上师": "", "售假币": "", "大麻": "",
    "售猎枪": "", "海luo因": "", "氯噻嗪": "", "逢八必灾": "", "原子弹方法": "", "逢9必乱": "", "西布曲明": "", "观音法门": "", "氧化汞": "", "轮功": "",
    "地西泮": "", "亚硒酸镁": "", "三唑仑": "", "电鸡": "", "k粉": "", "mdma": "", "fl功": "", "售麻醉": "", "退dang": "", "ketamine": "",
    "法轮": "", "诺查丹玛斯": "", "androst": "", "氧化二丁基锡": "", "明慧周报": "", "售狗子": "", "亚砷（酸）酐": "", "亚硝酸乙酯": "", "甲睾酮": "",
    "suicide": "",
    "集体自杀": "", "售左轮": "", "地塞米松": "", "李洪志": "", "testosterone": "", "电话窃听": "", "逢九必乱": "", "阿芙蓉": "", "原子弹清单": "",
    "售三棱": "",
    "大纪元": "", "9评": "", "枪的制": "", "枪出售": "", "鸦片": "", "退党": "", "枪货到": "", "售热武": "", "dajiyuan": "", "九评": "",
    "法0功": "", "法x功": "", "安非他命": "", "志洪李": "", "发论工": "", "正见网": "", "枪手": "", "diamorphine": "", "氵去车仑": "",
    "按照马雅历法": "",
    "售军用": "", "新型毒品": "", "朱瑟里诺": "", "售弹簧刀": "", "呋塞米": "", "逢8必灾": "", "枪销售": "", "冰毒": "", "尼可刹米": "", "盘古": "",
    "氧氯化磷": "", "电话交友": "", "cannabis": "", "strychnine": "", "法lun": "", "9ping": "", "安眠酮": "", "新唐人": "", "fa轮": "",
    "济世灵文": "",
    "售手枪": "", "苯丙胺": "", "亚硒酸": "", "电话追杀系统": "", "flg": "", "代血浆": "", "氧化亚铊": "", "轮子功": "", "轮法功": "", "地奈德": "",
    "促性腺激素": "", "李宏志": "", "售虎头": "", "枪械制": "", "法一轮一功": "", "tuidang": "", "zi杀": "", "超越红墙": "", "电话定位器": "",
    "海洛因": "",
    "凯他敏": "", "售一元硬": "", "藏字石": "", "亚硒酸二钠": "", "莫达非尼": "", "兴奋剂": "", "原装弹": "", "titor": "", "adrenaline": "",
    "cocain": "",
    "亚硒酸钠": "", "枪子弹": "", "氯胺酮": "", "泼尼松": "", "售火药": "", "吗啡": "", "推bei图": "", "售五四": "", "车仑工力": "", "gong和": "",
    "土g": "", "共x党": "", "gongchandang": "", "共残裆": "", "产党共": "", "共产专制": "", "国wu院": "", "政付": "", "土共": "", "共惨": "",
    "政俯": "", "腐败": "", "供铲党": "", "共铲": "", "老共": "", "gc党": "", "政腐": "", "公产党": "", "裆中央": "", "政f": "",
    "共产党专制": "", "共产党的报应": "", "gong党": "", "zhengfu": "", "中国zf": "", "共贪党": "", "供铲谠": "", "共匪": "", "共残党": "",
    "共残主义": "",
    "共产主义的幽灵": "", "共产王朝": "", "挡中央": "", "恶党": "", "症腐": "", "共产党的末日": "", "正府": "", "g产": "", "communistparty": "",
    "贡挡": "",
    "贪污": "", "供产": "", "共狗": "", "工产党": "", "中gong": "", "g匪": "", "政zhi": "", "gcd": "", "共产党腐败": "", "中珙": "",
    "档中央": "", "拱铲": "", "共c党": "", "供铲裆": "", "北京政权": "", "阿共": "", "仇共": "", "共一产一党": "", "中央zf": "", "中华帝国": "",
    "大陆官方": "", "邪党": "", "狗产蛋": "", "日你": "", "先人板板": "","江泽民":"","膜蛤":""
}


def check(request):
    content = request.GET.get('content') or request.POST.get('content')
    if not content:
        return JsonResponse({'result': 'fail'})
    print(content)
    s = jieba.cut(content,cut_all=True)
    str = '*'.join(s)
    jieba_list = str.split('*')
    print(jieba_list)
    jieba_list = [i for i in list(set(jieba_list)) if len(i) > 0]
    print(jieba_list)
    jieba_list.append(content)
    for k in jieba_list:
        if k in dict:
            content = content.replace(k, '*' * len(k))
    return JsonResponse({'result': 'ok', 'content': content})
