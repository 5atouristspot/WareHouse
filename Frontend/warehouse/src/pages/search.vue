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
              <el-button type="primary" icon="el-icon-search" @click="doSearch()">搜索</el-button>
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
            <div class="query-criteria-div" style="margin: 10px 30px;">
              <el-select v-model="retrospectSelect" placeholder="请选择">
                <el-option
                  v-for="item in retrospectOptions"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
              </el-select>
              <el-input class="search-input" v-model="retrospectInput" placeholder="请输入内容"></el-input>
              <el-button type="primary" icon="el-icon-search">搜索</el-button>
            </div>
            <div class="query-result-div" style="margin-top: 10px;">

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
      }
    },
    methods: {
      init() {

      }
    },
    methods: {
      doSearch() {
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
