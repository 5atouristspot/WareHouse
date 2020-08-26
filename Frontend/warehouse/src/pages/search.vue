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
                <el-table
                  :data="tableItem.list"
                  style="width: 100%"
                  row-key="id"
                  stripe
                  border
                  default-expand-all
                  :tree-props="{children: 'children', hasChildren: 'hasChildren'}">
                  <el-table-column
                    prop="id"
                    label="id"
                    width="180">
                  </el-table-column>
                  <el-table-column
                    prop="material"
                    label="material"
                    width="130">
                  </el-table-column>
                  <el-table-column
                    prop="material_description"
                    label="material_description">
                  </el-table-column>
                  <el-table-column
                    prop="order_num"
                    label="order_num"
                    width="130">
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
                    width="130">
                  </el-table-column>
                  <!--<el-table-column
                    prop="pid"
                    label="pid"
                    width="120">
                  </el-table-column>-->
                  <el-table-column
                    prop="posting_date"
                    label="posting_date"
                    width="150">
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
          }
        })
        // 临时假数据
        //this.tableData2 = [{"order_num":"101563","list":[{"id":158825,"material":"60010","material_description":"Silibinin Capsules 35mg","order_num":"101563","batch":"600903050","quantity_wi":975181.0,"unit":"EA","pid":0,"posting_date":"2016-08-22","children":[{"id":157823,"material":"10001","material_description":"silibinin","order_num":"101503","batch":"15000383","quantity_wi":35.0,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157825,"material":"20028","material_description":"Soya Lecithin","order_num":"101503","batch":"15000354","quantity_wi":0.39,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157826,"material":"20028","material_description":"Soya Lecithin","order_num":"101503","batch":"16000033","quantity_wi":64.61,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157828,"material":"20035","material_description":"Anhydrous Ethanol","order_num":"101503","batch":"16000029","quantity_wi":480.0,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157830,"material":"20035","material_description":"Anhydrous Ethanol","order_num":"101503","batch":"16000029","quantity_wi":20.0,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157832,"material":"20033","material_description":"Lactose (SpheroLac 100)","order_num":"101503","batch":"15000369","quantity_wi":106.0,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157834,"material":"20034","material_description":"Talc Powder","order_num":"101503","batch":"16000036","quantity_wi":31.46,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157836,"material":"20029","material_description":"Glycolys STD","order_num":"101503","batch":"16000006","quantity_wi":20.6,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157838,"material":"20036","material_description":"Silibinin printing 1#vacant capsules","order_num":"101503","batch":"15000366","quantity_wi":975395.0,"unit":"EA","pid":158825,"posting_date":"2016-05-09"}]},{"id":158827,"material":"30010","material_description":"PVC/PVDC Colorless 231mm","order_num":"101563","batch":"16000038","quantity_wi":175.2,"unit":"KG","pid":0,"posting_date":"2016-08-22"},{"id":158829,"material":"30011","material_description":"AluminumFoil231mm SilibininCapsules 35mg","order_num":"101563","batch":"16000026","quantity_wi":29.65,"unit":"KG","pid":0,"posting_date":"2016-08-22"},{"id":158831,"material":"30012","material_description":"Tropical Type Blister AluminumFoil 231mm","order_num":"101563","batch":"16000027","quantity_wi":96.91,"unit":"KG","pid":0,"posting_date":"2016-08-22"},{"id":158833,"material":"40018","material_description":"Silibinin Capsules Leaflet","order_num":"101563","batch":"16000025","quantity_wi":3244.0,"unit":"EA","pid":0,"posting_date":"2016-08-22"},{"id":158834,"material":"40018","material_description":"Silibinin Capsules Leaflet","order_num":"101563","batch":"16000044","quantity_wi":45495.0,"unit":"EA","pid":0,"posting_date":"2016-08-22"},{"id":158836,"material":"40019","material_description":"Silibinin Capsules 35mg*2*10EA Carton","order_num":"101563","batch":"16000068","quantity_wi":30509.0,"unit":"EA","pid":0,"posting_date":"2016-08-22"},{"id":158837,"material":"40019","material_description":"Silibinin Capsules 35mg*2*10EA Carton","order_num":"101563","batch":"16000085","quantity_wi":18226.0,"unit":"EA","pid":0,"posting_date":"2016-08-22"},{"id":158839,"material":"40010","material_description":"BOPP Film 178mm","order_num":"101563","batch":"16000013","quantity_wi":7.33,"unit":"KG","pid":0,"posting_date":"2016-08-22"},{"id":158840,"material":"40010","material_description":"BOPP Film 178mm","order_num":"101563","batch":"16000018","quantity_wi":8.36,"unit":"KG","pid":0,"posting_date":"2016-08-22"},{"id":158842,"material":"40020","material_description":"Silibinin Capsules 35mg*2*10EA Shipper","order_num":"101563","batch":"16000060","quantity_wi":8.0,"unit":"EA","pid":0,"posting_date":"2016-08-22"},{"id":158843,"material":"40020","material_description":"Silibinin Capsules 35mg*2*10EA Shipper","order_num":"101563","batch":"16000069","quantity_wi":157.0,"unit":"EA","pid":0,"posting_date":"2016-08-22"},{"id":158845,"material":"40021","material_description":"Silibinin Capsules35mg*2*10EA Paperboard","order_num":"101563","batch":"16000061","quantity_wi":336.0,"unit":"EA","pid":0,"posting_date":"2016-08-22"}]},{"order_num":"101632","list":[{"id":159935,"material":"40018","material_description":"Silibinin Capsules Leaflet","order_num":"101632","batch":"16000106","quantity_wi":32900.0,"unit":"EA","pid":0,"posting_date":"2016-08-22"},{"id":159937,"material":"40022","material_description":"Silibinin Capsules35mg*3*10EA Carton","order_num":"101632","batch":"16000110","quantity_wi":32655.0,"unit":"EA","pid":0,"posting_date":"2016-08-22"},{"id":159939,"material":"40010","material_description":"BOPP Film 178mm","order_num":"101632","batch":"16000075","quantity_wi":13.09,"unit":"KG","pid":0,"posting_date":"2016-08-22"},{"id":159941,"material":"40023","material_description":"Silibinin Capsules 35mg*3*10EA Shipper","order_num":"101632","batch":"16000093","quantity_wi":114.0,"unit":"EA","pid":0,"posting_date":"2016-08-22"},{"id":159942,"material":"40023","material_description":"Silibinin Capsules 35mg*3*10EA Shipper","order_num":"101632","batch":"16000119","quantity_wi":50.0,"unit":"EA","pid":0,"posting_date":"2016-08-22"},{"id":159944,"material":"40024","material_description":"Silibinin Capsules35mg*3*10EA Paperboard","order_num":"101632","batch":"16000094","quantity_wi":330.0,"unit":"EA","pid":0,"posting_date":"2016-08-22"},{"id":159945,"material":"70008","material_description":"Silibinin Capsules 35mg*2*10EA","order_num":"101632","batch":"650605018","quantity_wi":972700.0,"unit":"EA","pid":0,"posting_date":"2016-08-22","children":[{"id":158825,"material":"60010","material_description":"Silibinin Capsules 35mg","order_num":"101563","batch":"600903050","quantity_wi":975181.0,"unit":"EA","pid":159945,"posting_date":"2016-08-22","children":[{"id":157823,"material":"10001","material_description":"silibinin","order_num":"101503","batch":"15000383","quantity_wi":35.0,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157825,"material":"20028","material_description":"Soya Lecithin","order_num":"101503","batch":"15000354","quantity_wi":0.39,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157826,"material":"20028","material_description":"Soya Lecithin","order_num":"101503","batch":"16000033","quantity_wi":64.61,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157828,"material":"20035","material_description":"Anhydrous Ethanol","order_num":"101503","batch":"16000029","quantity_wi":480.0,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157830,"material":"20035","material_description":"Anhydrous Ethanol","order_num":"101503","batch":"16000029","quantity_wi":20.0,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157832,"material":"20033","material_description":"Lactose (SpheroLac 100)","order_num":"101503","batch":"15000369","quantity_wi":106.0,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157834,"material":"20034","material_description":"Talc Powder","order_num":"101503","batch":"16000036","quantity_wi":31.46,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157836,"material":"20029","material_description":"Glycolys STD","order_num":"101503","batch":"16000006","quantity_wi":20.6,"unit":"KG","pid":158825,"posting_date":"2016-05-09"},{"id":157838,"material":"20036","material_description":"Silibinin printing 1#vacant capsules","order_num":"101503","batch":"15000366","quantity_wi":975395.0,"unit":"EA","pid":158825,"posting_date":"2016-05-09"}]},{"id":158827,"material":"30010","material_description":"PVC/PVDC Colorless 231mm","order_num":"101563","batch":"16000038","quantity_wi":175.2,"unit":"KG","pid":159945,"posting_date":"2016-08-22"},{"id":158829,"material":"30011","material_description":"AluminumFoil231mm SilibininCapsules 35mg","order_num":"101563","batch":"16000026","quantity_wi":29.65,"unit":"KG","pid":159945,"posting_date":"2016-08-22"},{"id":158831,"material":"30012","material_description":"Tropical Type Blister AluminumFoil 231mm","order_num":"101563","batch":"16000027","quantity_wi":96.91,"unit":"KG","pid":159945,"posting_date":"2016-08-22"},{"id":158833,"material":"40018","material_description":"Silibinin Capsules Leaflet","order_num":"101563","batch":"16000025","quantity_wi":3244.0,"unit":"EA","pid":159945,"posting_date":"2016-08-22"},{"id":158834,"material":"40018","material_description":"Silibinin Capsules Leaflet","order_num":"101563","batch":"16000044","quantity_wi":45495.0,"unit":"EA","pid":159945,"posting_date":"2016-08-22"},{"id":158836,"material":"40019","material_description":"Silibinin Capsules 35mg*2*10EA Carton","order_num":"101563","batch":"16000068","quantity_wi":30509.0,"unit":"EA","pid":159945,"posting_date":"2016-08-22"},{"id":158837,"material":"40019","material_description":"Silibinin Capsules 35mg*2*10EA Carton","order_num":"101563","batch":"16000085","quantity_wi":18226.0,"unit":"EA","pid":159945,"posting_date":"2016-08-22"},{"id":158839,"material":"40010","material_description":"BOPP Film 178mm","order_num":"101563","batch":"16000013","quantity_wi":7.33,"unit":"KG","pid":159945,"posting_date":"2016-08-22"},{"id":158840,"material":"40010","material_description":"BOPP Film 178mm","order_num":"101563","batch":"16000018","quantity_wi":8.36,"unit":"KG","pid":159945,"posting_date":"2016-08-22"},{"id":158842,"material":"40020","material_description":"Silibinin Capsules 35mg*2*10EA Shipper","order_num":"101563","batch":"16000060","quantity_wi":8.0,"unit":"EA","pid":159945,"posting_date":"2016-08-22"},{"id":158843,"material":"40020","material_description":"Silibinin Capsules 35mg*2*10EA Shipper","order_num":"101563","batch":"16000069","quantity_wi":157.0,"unit":"EA","pid":159945,"posting_date":"2016-08-22"},{"id":158845,"material":"40021","material_description":"Silibinin Capsules35mg*2*10EA Paperboard","order_num":"101563","batch":"16000061","quantity_wi":336.0,"unit":"EA","pid":159945,"posting_date":"2016-08-22"}]}]}];
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
</style>
