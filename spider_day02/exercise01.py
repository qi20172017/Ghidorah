import re
html1 = """
<li class="cards-li list-photo-li" name="lazyloadcpc" id="shucar_36180101" isfin="0" brandid="42" seriesid="3720" linktype="3" publicdate="2020-01-02T10:00:04Z" iscpl="0" iscxlm="0" fromtype="40" islimit="0" isafteraudit="10" abtest="10" order="0" isrecom="0" infoid="36180101" carname="法拉利488 2018款 488 Pista" price="469.8" cid="110100" pid="110000" milage="0.01" regdate="1900/01" specid="33587" dealerid="117231" isnewcar="1" iscredit="0" isextendrepair="0" isfactory="2" page="55" pos="52" filter="0aa0_0a0_0a0_0" bucket="" recomid="0" refreshid="0" cartype="70" queryid="">  
                       <a href="/dealer/117231/36180101.html?pvareaid=100519&amp;userpid=110000&amp;usercid=110100#pos=52#page=55#rtype=10#isrecom=0#filter=0aa0_0a0_0a0_0#module=10#refreshid=0#recomid=0#queryid=#cartype=70" class="carinfo" target="_blank">
                        
                                <div class="img-box">
                                
                            <img name="lazyloadImg" alt="法拉利488 2018款 488 Pista" src="//2sc2.autoimg.cn/escimg/g28/M0A/1B/65/f_440x0_0_q87_autohomecar__ChsEnl4IQ3SAVJFTAAGBH2OWzVY068.jpg" src2="//2sc2.autoimg.cn/escimg/g28/M0A/1B/65/f_440x0_0_q87_autohomecar__ChsEnl4IQ3SAVJFTAAGBH2OWzVY068.jpg" onerror="javascript:this.src='//www.autoimg.cn/2scimg/web/website/20160112/default-diagram.jpg';"></div>
                        
                        <div class="cards-bottom">
                            <h4 class="card-name">法拉利488 2018款 488 Pista</h4>
                            <p class="cards-unit">0.01万公里／未上牌／北京／商家</p>
                            <div class="cards-price-box">
                                <span class="pirce"><em>469.80</em>万</span><span class="tags"><i class="tp-tags green" title="车辆为车龄2年、行驶里程4万公里以内">准新车</i><i class="tp-tags green" title="车辆过户次数为0">0次过户</i></span><s>442.87万</s> 
                            </div>
                        </div>
                    </a> 			
                </li>
"""

html2 = """
<div class="car-box">
        <h3 class="car-brand-name">奔驰G级 2017款 G500 4x4</h3>
        <div class="car-tags tags"><i class="tp-tags white">准新车<div class="tag-content">车辆为车龄2年、行驶里程4万公里以内</div></i><i class="tp-tags white">0次过户<div class="tag-content">车辆过户次数为0</div></i></div>
        <ul class="brand-unit-item fn-clear">
            <li>
                <p>行驶里程</p>
                <h4>0.01万公里</h4>
            </li>
            <li>
                <p>上牌时间</p>
                <h4>未上牌</h4>
            </li>
            <li>
                <p>挡位 / 排量</p>
                <h4>自动 / 4L</h4>
            </li>
            <li>
                <p>车辆所在地</p>
                <h4>北京</h4>
            </li>
            <li>
                <p><a target="_blank" href="https://www.che168.com/norm.html#pvareaid=100953">查看限迁地<i class="usedfont used-youjiantou"></i></a></p>
                <h4>-
                    <i class="ico-explain">
                        <div class="explain-content">
                            排放标准请以各地车管所认定为准，此标准<br>
                            仅供参考，外迁请详细咨询迁入车管所。
                        </div>
                    </i></h4>
            </li>
        </ul>
        
        <div class="brand-price-item">
            <a id="noticeprice" name="track" eventkey="c_pc_2sc_cardetail_jjtz" href="javascript:void(0)" class="right-item subscription">订阅降价通知</a>
            <span class="price" id="overlayPrice">￥249.80<b>万</b><i class="usedfont used-xiajiantou" style="display: none;"></i>
                <div class="price-overlay fn-hide" id="overlay1">
                    <div class="overlay-head">
                        <p id="base_compprice" style="display: none"></p>
                        <p id="CarNewPrice" style="display: none"></p>
                        <p id="spanReferencePrice" style="display: none"></p>
                    </div>
                </div>
                </span>
            <em class="price-transfer ndy">含购置税</em>
              
            <s class="price-nom" id="newprice" style="display: none;">新车含税价:0万</s>
            
        </div>
        
        <div id="div_btn_fenqigou" class="business-item mt20" style="display:none;">
            <a name="track" eventkey="c_pc_detail_loan" infoid="33304168" href="https://www.che168.com/applyfinanial/33304168.html?pvareaid=108766" target="_blank"><em class="right-arrow">立即申请<i class="usedfont used-youjiantou"></i></em>
                <i class="business-tags orange">分期购</i><b class="b-fw b-gray b-bold">首付<u>74.94万</u></b><span class="text-gray">月供低至6.22万元</span>
            </a>
        </div>
        
        <div class="business-item  fn-hide" id="favorite_item">
            <a href="javascript:void(0);" id="b_favorite"><em class="right-arrow" id="ischange">收藏该车<i class="usedfont used-youjiantou"></i></em>
                <b class="b-fw no-mr" id="favoritenum">该车已被<u>102人</u>收藏，</b><span class="text-gray text-gray2 " id="favortspan">快人一步马上行动→</span>
            </a>
        </div>
        
        <div class="business-item fn-hide" id="askprice_item" style="">
            <a href="javascript:void(0);" id="item_askprice" class="askprice"><em class="right-arrow">咨询车主<i class="usedfont used-youjiantou"></i></em>
                <b class="b-fw no-mr">该车价格低于<u id="pricenum">6%</u>的同系车辆，</b><span class="text-gray text-gray2">去找车主询个价</span>
            </a>
        </div>
        
        <div class="bottom-btn-item">
            <a id="askprice" href="javascript:void(0);" class="askprice tp-btn tp-btn-big">我要砍价</a>
            
            <a href="javascript:void(0)" class="tp-btn tp-btn-cancel tp-btn-big xphone_button_mini" id="xphonerigger" data-title="">查看电话
                   <!--查看电话弹窗-->
                <div id="miniProBox" class="tp-tip fn-hide" dealerid="117231" infoid="33304168" price="249.8000">
                    <div class="code-tip-box">
                        <p class="xiphone-tip">请拨打电话号码</p>
                        <p id="xphone_button_mini" class="phone"></p>
                        <p>
                            <img id="miniProimg" src="">
                        </p>
                        <p class="bottom-text">微信扫一扫，免手动输入</p>
                    </div>
                    <span class="tip-arrow tip-bottom"></span>
                </div>
            </a>
        </div>

    </div>

"""

html1_1 = """
<li class="cards-li list-photo-li".*?<a href="(.*?)".*?</li>
"""

pattren = re.compile(html1_1,re.S)
print(pattren.findall(html1))