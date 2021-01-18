<template>
  <div id="supplier">
    <GoBack v-bind:target="target"/>
    <div class="content-div global-bg-color">
      <div class="supplier-div">
        <el-tabs type="border-card">
          <el-tab-pane label="搜索" class="my-tab-pane">
            <div class="query-criteria-div" style="margin: 20px 30px 10px 30px;">
              <el-select v-model="supplierSelect" placeholder="请选择">
                <el-option
                  v-for="item in supplierOptions"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
              <el-input class="supplier-input" v-model="supplierInput" placeholder="请输入内容"></el-input>
              <el-button type="primary" icon="el-icon-supplier" @click="doSupplier()">搜索</el-button>
            </div>
            <div class="query-result-div" style="margin: 20px;">
              <el-table
                :cell-style="getCellStyle"
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
                  prop="supply_type"
                  label="供货类型">
                </el-table-column>
                <el-table-column
                  prop="material"
                  label="物料号">
                </el-table-column>
                <el-table-column
                  prop="material_description"
                  label="物料描述">
                </el-table-column>
                <el-table-column
                  prop="unit"
                  label="单位">
                </el-table-column>
                <el-table-column
                  prop="supplier"
                  label="供应商">
                </el-table-column>
                <el-table-column
                  prop="sante_material_requirements_mon"
                  label="圣特物料需求月份"
                  width="90">
                </el-table-column>
                <el-table-column
                  prop="sante_material_requirements"
                  label="圣特物料需求"
                  width="90">
                </el-table-column>
                <el-table-column
                  prop="supplier_inventory"
                  label="供应商库存（已备货）">
                </el-table-column>
                <el-table-column
                  prop="supplier_production_quantity"
                  label="供应商在产数量">
                </el-table-column>
                <el-table-column
                  prop="estimate_completion_time"
                  label="预计完成时间">
                </el-table-column>
                <el-table-column
                  prop="gap"
                  label="gap">
                </el-table-column>
                <!--
                <el-table-column
                  prop="sante_arrival_time"
                  label="圣特到货时间">
                </el-table-column>
                <el-table-column
                  prop="supplier_delivery_time"
                  label="供应商发货时间">
                </el-table-column>
                -->
              </el-table>
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
    name: 'supplier',
    data() {
      return {
        target: '/plan',
        supplierInput: '',
        supplierSelect: '',
        supplierOptions: [{
          value: 'material',
          label: '物料编码'
        }, {
          value: 'material_description',
          label: '物料描述'
        }, {
          value: 'supplier',
          label: '供应商'
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
      doSupplier() {
        let supplierReqParams = {
          search_type: this.supplierSelect,
          search_keys: this.supplierInput,
          token: localStorage.token
        }
        this.$axios.defaults.auth = {
          username: localStorage.token,
          password: 'unused'
        }
        this.$axios.get('/api/v1000/elevated/suppliermanagement', {params : supplierReqParams}).then(res => {
          let data = res.data
          if (data && data.length > 0) {
            this.tableData1 = data
          }
        })
        // 临时假数据
        /*this.tableData1 = [];
        let data = "[{\"id\":1,\"supply_type\":\"\u751f\u4ea7\u5546\",\"material\":\"10001\",\"material_description\":\"\u6c34\u98de\u84df\u5bbe\",\"unit\":\"KG\",\"supplier\":\"\u5e1d\u76ca\",\"sante_material_requirements_mon\":\"12\u6708\u4efd\",\"sante_material_requirements\":\"1200.0\",\"supplier_inventory\":\"1200.0\",\"supplier_production_quantity\":\"\",\"estimate_completion_time\":\"0\",\"gap\":0.0},{\"id\":2,\"supply_type\":\"\u751f\u4ea7\u5546\",\"material\":\"10001\",\"material_description\":\"\u6c34\u98de\u84df\u5bbe\",\"unit\":\"KG\",\"supplier\":\"\u5e1d\u76ca\",\"sante_material_requirements_mon\":\"1\u6708\u4efd\",\"sante_material_requirements\":\"1200.0\",\"supplier_inventory\":\"1200.0\",\"supplier_production_quantity\":\"\",\"estimate_completion_time\":\"0\",\"gap\":0.0},{\"id\":3,\"supply_type\":\"\u751f\u4ea7\u5546\",\"material\":\"10001\",\"material_description\":\"\u6c34\u98de\u84df\u5bbe\",\"unit\":\"KG\",\"supplier\":\"\u5e1d\u76ca\",\"sante_material_requirements_mon\":\"2\u6708\u4efd\",\"sante_material_requirements\":\"800.0\",\"supplier_inventory\":\"400.0\",\"supplier_production_quantity\":\"1600.0\",\"estimate_completion_time\":\"2021-01-04\",\"gap\":-400.0}]";
        this.tableData1 = JSON.parse(data);
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
      getCellStyle ({row, column, rowIndex, columnIndex}) {
        let specialCellName = 'gap'
        if (row[specialCellName] != 0 && column.property == specialCellName) {
          return "color: #111111; background-color: #ff99cc; border-color: #ff99cc;"
        }
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
  .supplier-div {
    width: 95%;
    margin: 0 auto;
  }
  .supplier-div .el-tabs__item {
    font-size: 20px;
    height: 50px;
    line-height: 50px;
  }
  .el-tabs--border-card>.el-tabs__header .el-tabs__item.is-active{
    color: #1890ff;
    font-weight: 600;
  }
  .supplier-div .el-tabs {
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
  .query-criteria-div .supplier-input {
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
  .supplier-div .el-table{
    font-size: 16px;
  }

  .supplier-div .el-table thead {
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
    background-color: #EEE;
  }
  .table-tips {
    font-size: 16px;
    font-weight: 600;
  }
</style>
