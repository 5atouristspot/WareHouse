<template>
  <div id="search">
    <GoBack v-bind:target="target"/>
    <div class="content-div global-bg-color">
      <div class="search-div">
        <el-tabs type="border-card">
          <el-tab-pane label="搜索" class="my-tab-pane">
            <div class="query-criteria-div" style="margin: 20px 30px 10px 30px;">
              <el-select v-model="searchSelect" placeholder="请选择">
                <el-option
                  v-for="item in searchOptions"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
              <el-input class="search-input" v-model="searchInput" placeholder="请输入内容"></el-input>
              <el-button type="primary" icon="el-icon-search" @click="doSearch1()">搜索</el-button>
            </div>
            <div class="query-result-div" style="margin: 20px;">
              <el-table
                :data="tableData1"
                style="width: 100%"
                row-key="id"
                stripe
                border>
                <el-table-column
                  prop="id"
                  label="id"
                  width="90">
                </el-table-column>
                <el-table-column
                  prop="material"
                  label="material">
                </el-table-column>
                <el-table-column
                  prop="storage_bin"
                  label="storage_bin">
                </el-table-column>
                <el-table-column
                  prop="batch"
                  label="batch">
                </el-table-column>
                <el-table-column
                  prop="material_desc"
                  label="material_desc">
                </el-table-column>
                <el-table-column
                  prop="avail_stock"
                  label="avail_stock">
                </el-table-column>
                <el-table-column
                  prop="unit"
                  label="unit"
                  width="90">
                </el-table-column>
                <el-table-column
                  prop="last_goods_rec"
                  label="last_goods_rec">
                </el-table-column>
                <el-table-column
                  prop="date_of_manuf"
                  label="date_of_manuf">
                </el-table-column>
                <el-table-column
                  prop="sled_bbd"
                  label="sled_bbd">
                </el-table-column>
                <el-table-column
                  prop="next_inspection"
                  label="next_inspection">
                </el-table-column>
                <el-table-column
                  prop="inventory_time"
                  label="inventory_time">
                </el-table-column>
                <el-table-column
                  prop="status"
                  label="status">
                </el-table-column>
              </el-table>
            </div>
          </el-tab-pane>
          <el-tab-pane label="物料追溯">
            <div class="query-criteria-div" style="margin: 20px 30px 10px 30px;">
              <!--<el-select v-model="retrospectSelect" placeholder="请选择">
                <el-option
                  v-for="item in retrospectOptions"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>-->
              <el-input class="search-input" v-model="retrospectInput" placeholder="请输入内容"></el-input>
              <el-button type="primary" icon="el-icon-search" @click="doSearch2()">搜索</el-button>
            </div>
            <div class="query-result-div" style="margin-top: 10px;">
              <div v-for="tableItem in tableData2">
                <div class="table-tips">成品信息</div>
                <el-table
                  :data="tableItem.finish_product_info"
                  style="width: 100%;"
                  row-key="id"
                  header-row-class-name="tableHeaderClass_cp"
                  border>
                  <el-table-column
                    prop="id"
                    label="id"
                    width="160">
                  </el-table-column>
                  <el-table-column
                    prop="material"
                    label="material"
                    width="120">
                  </el-table-column>
                  <el-table-column
                    prop="material_description"
                    label="material_description">
                  </el-table-column>
                  <el-table-column
                    prop="order_num"
                    label="order_num"
                    width="120">
                  </el-table-column>
                  <el-table-column
                    prop="batch"
                    label="batch"
                    width="130">
                  </el-table-column>
                  <el-table-column
                    prop="quantity_wi"
                    label="quantity_wi"
                    width="130">
                  </el-table-column>
                  <el-table-column
                    prop="unit"
                    label="unit"
                    width="90">
                  </el-table-column>
                  <el-table-column
                    prop="creating_date"
                    label="Products_date"
                    width="130">
                  </el-table-column>
                  <el-table-column
                    prop="consuming_date"
                    label="Consuming_date"
                    width="150">
                  </el-table-column>
                  <el-table-column
                    prop="gaining_date"
                    label="Good Receipt_date"
                    width="130">
                  </el-table-column>
                  <el-table-column
                    prop="pasting_date"
                    label="Release_date"
                    width="130">
                  </el-table-column>
                </el-table>
                <div class="table-tips">组成物料</div>
                <el-table
                  :data="tableItem.list"
                  style="width: 100%; margin-bottom: 30px;"
                  row-key="id"
                  border
                  default-expand-all
                  header-row-class-name="tableHeaderClass"
                  :tree-props="{children: 'children', hasChildren: 'hasChildren'}">
                  <el-table-column
                    prop="id"
                    label="id"
                    width="160">
                  </el-table-column>
                  <el-table-column
                    prop="material"
                    label="material"
                    width="120">
                  </el-table-column>
                  <el-table-column
                    prop="material_description"
                    label="material_description">
                  </el-table-column>
                  <el-table-column
                    prop="order_num"
                    label="order_num"
                    width="120">
                  </el-table-column>
                  <el-table-column
                    prop="batch"
                    label="batch"
                    width="130">
                  </el-table-column>
                  <el-table-column
                    prop="quantity_wi"
                    label="quantity_wi"
                    width="130">
                  </el-table-column>
                  <el-table-column
                    prop="unit"
                    label="unit"
                    width="90">
                  </el-table-column>
                  <el-table-column
                    prop="creating_date"
                    label="Products_date"
                    width="130">
                  </el-table-column>
                  <el-table-column
                    prop="consuming_date"
                    label="Consuming_date"
                    width="150">
                  </el-table-column>
                  <el-table-column
                    prop="gaining_date"
                    label="Good Receipt_date"
                    width="130">
                  </el-table-column>
                  <el-table-column
                    prop="pasting_date"
                    label="Release_date"
                    width="130">
                  </el-table-column>
                </el-table>
                <br>
              </div>
            </div>
          </el-tab-pane>
        </el-tabs>
      </div>
    </div>
  </div>
</template>

<script>
  import GoBack from '@/components/GoBack'
  export default {
    name: 'search',
    data() {
      return {
        target: '/plan',
        searchInput: '',
        searchSelect: '',
        searchOptions: [{
          value: 'storage_bin',
          label: 'Storage Bin'
        }, {
          value: 'material',
          label: '物料名'
        }, {
          value: 'batch',
          label: '批号'
        }, {
          value: 'material_desc',
          label: '物料描述'
        }],
        retrospectInput: '',
        retrospectSelect: '',
        retrospectOptions: [{
          value: '1',
          label: '批号'
        }, {
          value: '2',
          label: '物料号'
        }],
        tableData1:[],
        tableData2:[],
      }
    },
    methods: {
      init() {

      },
      doSearch1() {
        let searchReqParams = {
          search_type: this.searchSelect,
          search_keys: this.searchInput,
          token: localStorage.token
        }
        this.$axios.defaults.auth = {
          username: localStorage.token,
          password: 'unused'
        }
        this.$axios.get('/api/v1000/elevated/searchinfo', {params : searchReqParams}).then(res => {
          let data = res.data
          if (data && data.length > 0) {
            this.tableData1 = data
          }
        })
        // 临时假数据
        /*this.tableData1 = [];
        for (let i = 0; i < 20; i++) {
          let item = {
            "id":6160 + i,
            "material":"NA",
            "storage_bin":"04-01-17",
            "batch":"1702001",
            "material_desc":"100ml瓶盖",
            "avail_stock":"1657.0",
            "unit":"EA",
            "last_goods_rec":"2019-04-15",
            "date_of_manuf":"2017-01-12",
            "sled_bbd":"0",
            "next_inspection":"0"
          }
          this.tableData1.push(item);
        }*/
      },
      doSearch2() {
        let retrospectReqParams = {
          batch: this.retrospectInput
        }
        this.$axios.defaults.auth = {
          username: localStorage.token,
          password: 'unused'
        }
        this.$axios.get('/api/v1000/elevated/materialtrace', {params : retrospectReqParams}).then(res => {
          let data = res.data
          if (data && data.length > 0) {
            this.tableData2 = data
            for (let i = 0; i < this.tableData2.length; i++) {
              let finishProductInfo = this.tableData2[i].finish_product_info;
              this.tableData2[i].finish_product_info = [finishProductInfo];
            }
          }
        })
        // 临时假数据
        /*this.tableData2 = [{"order_num":"101563","finish_product_info":{"id":24680,"material":"70008","material_description":"Silibinin Capsules 35mg*2*10EA","order_num":"101563","batch":"650605018","quantity_wi":972700,"unit":"EA","creating_date":"2016-05-09","consuming_date":"","gaining_date":"","pasting_date":"2016-05-16"},"list":[{"id":24645,"material":"30010","material_description":"PVC/PVDC Colorless 231mm","order_num":"101563","batch":"16000038","quantity_wi":175,"unit":"KG","pid":0,"creating_date":"","consuming_date":"2016-05-09","gaining_date":"","pasting_date":""},{"id":24647,"material":"30011","material_description":"AluminumFoil231mm SilibininCapsules 35mg","order_num":"101563","batch":"16000026","quantity_wi":29,"unit":"KG","pid":0,"creating_date":"","consuming_date":"2016-05-09","gaining_date":"","pasting_date":""},{"id":24652,"material":"30012","material_description":"Tropical Type Blister AluminumFoil 231mm","order_num":"101563","batch":"16000027","quantity_wi":96,"unit":"KG","pid":0,"creating_date":"","consuming_date":"2016-05-09","gaining_date":"","pasting_date":""},{"id":24654,"material":"40010","material_description":"BOPP Film 178mm","order_num":"101563","batch":"16000018","quantity_wi":8,"unit":"KG","pid":0,"creating_date":"","consuming_date":"2016-05-09","gaining_date":"","pasting_date":""},{"id":24656,"material":"40010","material_description":"BOPP Film 178mm","order_num":"101563","batch":"16000013","quantity_wi":7,"unit":"KG","pid":0,"creating_date":"","consuming_date":"2016-05-09","gaining_date":"","pasting_date":""},{"id":24657,"material":"40018","material_description":"Silibinin Capsules Leaflet","order_num":"101563","batch":"16000044","quantity_wi":45495,"unit":"EA","pid":0,"creating_date":"","consuming_date":"2016-05-09","gaining_date":"","pasting_date":""},{"id":24658,"material":"40018","material_description":"Silibinin Capsules Leaflet","order_num":"101563","batch":"16000025","quantity_wi":3244,"unit":"EA","pid":0,"creating_date":"","consuming_date":"2016-05-09","gaining_date":"","pasting_date":""},{"id":24662,"material":"40019","material_description":"Silibinin Capsules 35mg*2*10EA Carton","order_num":"101563","batch":"16000085","quantity_wi":18226,"unit":"EA","pid":0,"creating_date":"","consuming_date":"2016-05-09","gaining_date":"","pasting_date":""},{"id":24663,"material":"40019","material_description":"Silibinin Capsules 35mg*2*10EA Carton","order_num":"101563","batch":"16000068","quantity_wi":30509,"unit":"EA","pid":0,"creating_date":"","consuming_date":"2016-05-09","gaining_date":"","pasting_date":""},{"id":24665,"material":"40020","material_description":"Silibinin Capsules 35mg*2*10EA Shipper","order_num":"101563","batch":"16000060","quantity_wi":8,"unit":"EA","pid":0,"creating_date":"","consuming_date":"2016-05-09","gaining_date":"","pasting_date":""},{"id":24666,"material":"40020","material_description":"Silibinin Capsules 35mg*2*10EA Shipper","order_num":"101563","batch":"16000069","quantity_wi":157,"unit":"EA","pid":0,"creating_date":"","consuming_date":"2016-05-09","gaining_date":"","pasting_date":""},{"id":24671,"material":"40021","material_description":"Silibinin Capsules35mg*2*10EA Paperboard","order_num":"101563","batch":"16000061","quantity_wi":336,"unit":"EA","pid":0,"creating_date":"","consuming_date":"2016-05-09","gaining_date":"","pasting_date":""},{"id":24676,"material":"60010","material_description":"Silibinin Capsules 35mg","order_num":"101563","batch":"600903050","quantity_wi":975181,"unit":"EA","pid":0,"creating_date":"","consuming_date":"2016-05-09","gaining_date":"","pasting_date":"","children":[{"id":23841,"material":"10001","material_description":"silibinin","order_num":"101503","batch":"15000383","quantity_wi":35,"unit":"KG","pid":24676,"creating_date":"","consuming_date":"2016-03-30","gaining_date":"","pasting_date":""},{"id":23850,"material":"20028","material_description":"Soya Lecithin","order_num":"101503","batch":"15000354","quantity_wi":0,"unit":"KG","pid":24676,"creating_date":"","consuming_date":"2016-03-30","gaining_date":"","pasting_date":""},{"id":23851,"material":"20028","material_description":"Soya Lecithin","order_num":"101503","batch":"16000033","quantity_wi":64,"unit":"KG","pid":24676,"creating_date":"","consuming_date":"2016-03-30","gaining_date":"","pasting_date":""},{"id":23862,"material":"20029","material_description":"Glycolys STD","order_num":"101503","batch":"16000006","quantity_wi":20,"unit":"KG","pid":24676,"creating_date":"","consuming_date":"2016-03-30","gaining_date":"","pasting_date":""},{"id":23870,"material":"20033","material_description":"Lactose (SpheroLac 100)","order_num":"101503","batch":"15000369","quantity_wi":106,"unit":"KG","pid":24676,"creating_date":"","consuming_date":"2016-03-30","gaining_date":"","pasting_date":""},{"id":23877,"material":"20034","material_description":"Talc Powder","order_num":"101503","batch":"16000036","quantity_wi":31,"unit":"KG","pid":24676,"creating_date":"","consuming_date":"2016-03-30","gaining_date":"","pasting_date":""},{"id":24116,"material":"20035","material_description":"Anhydrous Ethanol","order_num":"101503","batch":"16000029","quantity_wi":20,"unit":"KG","pid":24676,"creating_date":"","consuming_date":"2016-04-18","gaining_date":"","pasting_date":""},{"id":24123,"material":"20036","material_description":"Silibinin printing 1#vacant capsules","order_num":"101503","batch":"15000366","quantity_wi":975395,"unit":"EA","pid":24676,"creating_date":"","consuming_date":"2016-04-18","gaining_date":"","pasting_date":""}]}]},{"order_num":"101632","finish_product_info":{"id":25749,"material":"70009","material_description":"Silibinin Capsules 35mg*3*10EA","order_num":"101632","batch":"650605018","quantity_wi":969450,"unit":"EA","creating_date":"2016-08-18","consuming_date":"","gaining_date":"","pasting_date":"2016-08-22"},"list":[{"id":25735,"material":"40010","material_description":"BOPP Film 178mm","order_num":"101632","batch":"16000075","quantity_wi":13,"unit":"KG","pid":0,"creating_date":"","consuming_date":"2016-08-18","gaining_date":"","pasting_date":""},{"id":25737,"material":"40018","material_description":"Silibinin Capsules Leaflet","order_num":"101632","batch":"16000106","quantity_wi":32900,"unit":"EA","pid":0,"creating_date":"","consuming_date":"2016-08-18","gaining_date":"","pasting_date":""},{"id":25740,"material":"40022","material_description":"Silibinin Capsules35mg*3*10EA Carton","order_num":"101632","batch":"16000110","quantity_wi":32655,"unit":"EA","pid":0,"creating_date":"","consuming_date":"2016-08-18","gaining_date":"","pasting_date":""},{"id":25741,"material":"40023","material_description":"Silibinin Capsules 35mg*3*10EA Shipper","order_num":"101632","batch":"16000119","quantity_wi":50,"unit":"EA","pid":0,"creating_date":"","consuming_date":"2016-08-18","gaining_date":"","pasting_date":""},{"id":25742,"material":"40023","material_description":"Silibinin Capsules 35mg*3*10EA Shipper","order_num":"101632","batch":"16000093","quantity_wi":114,"unit":"EA","pid":0,"creating_date":"","consuming_date":"2016-08-18","gaining_date":"","pasting_date":""},{"id":25745,"material":"40024","material_description":"Silibinin Capsules35mg*3*10EA Paperboard","order_num":"101632","batch":"16000094","quantity_wi":330,"unit":"EA","pid":0,"creating_date":"","consuming_date":"2016-08-18","gaining_date":"","pasting_date":""},{"id":25746,"material":"70008","material_description":"Silibinin Capsules 35mg*2*10EA","order_num":"101632","batch":"650605018","quantity_wi":972700,"unit":"EA","pid":0,"creating_date":"2016-08-18","consuming_date":"2016-08-18","gaining_date":"","pasting_date":"2016-08-22"}]}];

        for (let i = 0; i < this.tableData2.length; i++) {
          let finishProductInfo = this.tableData2[i].finish_product_info
          this.tableData2[i].finish_product_info = [finishProductInfo]
        }*/

      }
    },
    components: {
      GoBack: GoBack
    },
    created() {
      this.init()
    }
  }
</script>

<style>
  .content-div {
    width: 100%;
  }
  .search-div {
    width: 95%;
    margin: 0 auto;
  }
  .search-div .el-tabs__item {
    font-size: 20px;
    height: 50px;
    line-height: 50px;
  }
  .el-tabs--border-card>.el-tabs__header .el-tabs__item.is-active{
    color: #1890ff;
    font-weight: 600;
  }
  .search-div .el-tabs {
    position: absolute;
    width: 95%;
    min-height: calc(100% - 150px);
    /*height: calc(100% - 150px);*/
  }
  .query-criteria-div {
    line-height: normal;
    display: inline-table;
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    text-align: center;
  }
  .query-criteria-div .search-input {
    width: 60%;
    margin: 0 10px;
  }
  .query-criteria-div .el-select .el-input {
    width: 180px;
  }
  .query-criteria-div .input-with-select .el-input-group__prepend {
    border: 1px solid #C0C4CC;
    background-color: #fff;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    margin-right: 10px;
  }
  .query-criteria-div .el-input,.el-select-dropdown__item {
    font-size: 20px;
  }

  .query-criteria-div .el-input__inner{
    color: #333333 !important;
    border-color: #C0C4CC;
    border-radius: 4px !important;
    height: 50px;
  }
  .query-criteria-div .el-button--primary {
    color: #000000 !important;
    font-size: 20px !important;
    background-color: #1890ff !important;
    border-color: #1890ff !important;
    height: 50px;
  }
  .search-div .el-table{
    font-size: 16px;
  }

  .search-div .el-table thead {
    color: #515a6e;
  }
  .query-result-div .el-table__row--level-1{
    background: #00BFFF;
  }
  .query-result-div .el-table__body .el-table__row--level-1:hover>td{
    background-color: #00BFFF!important;
  }
  .query-result-div .el-table__body .el-table__row--level-1.current-row>td{
    background-color: #00BFFF!important;
  }

  .query-result-div .el-table__row--level-2{
    background: #00FF7F;
  }
  .query-result-div .el-table__body .el-table__row--level-2:hover>td{
    background-color: #00FF7F!important;
  }
  .query-result-div .el-table__body .el-table__row--level-2.current-row>td{
    background-color: #00FF7F!important;
  }

  .query-result-div .el-table__row--level-3{
    background: #FFFF00;
  }
  .query-result-div .el-table__body .el-table__row--level-3:hover>td{
    background-color: #FFFF00!important;
  }
  .query-result-div .el-table__body .el-table__row--level-3.current-row>td{
    background-color: #FFFF00!important;
  }

  .query-result-div .el-table__row--level-4{
    background: #9932CC;
  }
  .query-result-div .el-table__body .el-table__row--level-4:hover>td{
    background-color: #9932CC!important;
  }
  .query-result-div .el-table__body .el-table__row--level-4.current-row>td{
    background-color: #9932CC!important;
  }

  .query-result-div .el-table {
    color: black;
  }
  .tableHeaderClass th {
    background-color: #EEE !important;
  }
  .tableHeaderClass_cp th {
    background-color: #B0E0E6 !important;
  }
  .table-tips {
    font-size: 16px;
    font-weight: 600;
    text-align: left;
  }
</style>
