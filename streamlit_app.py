<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CleanWave Laundry System</title>
<link href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<style>
/* ═══════════════════════════════════════════════════════════
   BASE
═══════════════════════════════════════════════════════════ */
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Nunito',sans-serif;min-height:100vh;color:#0F172A;overflow-x:hidden}

/* ═══════════════════════════════════════════════════════════
   SHARED COMPONENTS
═══════════════════════════════════════════════════════════ */
.card{background:#fff;border-radius:16px;padding:24px;box-shadow:0 2px 12px rgba(0,0,0,.06);margin-bottom:20px}
.card-sm{background:#fff;border-radius:12px;padding:16px;box-shadow:0 1px 6px rgba(0,0,0,.06)}
.title{font-size:22px;font-weight:800;color:#0369A1;margin-bottom:4px}
.subtitle{font-size:14px;color:#64748B;margin-bottom:20px}
.label{font-size:13px;font-weight:600;color:#374151;display:block;margin-bottom:4px}
.input,.textarea{width:100%;padding:10px 14px;border-radius:10px;border:1.5px solid #E2E8F0;font-family:inherit;font-size:14px;outline:none;transition:border-color .2s}
.input:focus,.textarea:focus{border-color:#0EA5E9}
.textarea{resize:vertical;min-height:70px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.grid3{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px}
.grid4{display:grid;grid-template-columns:1fr 1fr 1fr 1fr;gap:14px}
.table{width:100%;border-collapse:collapse}
.th{padding:10px 14px;text-align:left;font-size:12px;font-weight:700;color:#64748B;border-bottom:2px solid #E2E8F0;text-transform:uppercase;letter-spacing:.5px}
.td{padding:11px 14px;font-size:14px;border-bottom:1px solid #F1F5F9;vertical-align:middle}
.badge{padding:3px 10px;border-radius:99px;font-size:12px;font-weight:700;display:inline-block}
.hidden{display:none!important}
.divider{border:none;border-top:1.5px dashed #E2E8F0;margin:14px 0}
.mb4{margin-bottom:4px} .mb8{margin-bottom:8px} .mb12{margin-bottom:12px} .mb14{margin-bottom:14px} .mb16{margin-bottom:16px} .mb20{margin-bottom:20px}

/* Buttons */
.btn{background:linear-gradient(135deg,#0EA5E9,#0369A1);color:#fff;border:none;padding:10px 20px;border-radius:10px;cursor:pointer;font-family:inherit;font-size:14px;font-weight:700;transition:all .2s;display:inline-flex;align-items:center;gap:6px}
.btn:hover{transform:translateY(-1px);box-shadow:0 4px 14px rgba(14,165,233,.4)}
.btn:active{transform:none}
.btn.sm{padding:6px 14px;font-size:13px;border-radius:8px}
.btn.lg{padding:13px 28px;font-size:15px}
.btn.block{width:100%;justify-content:center}
.btn.secondary{background:#F1F5F9;color:#374151}
.btn.secondary:hover{background:#E2E8F0;box-shadow:none}
.btn.success{background:linear-gradient(135deg,#10B981,#059669)}
.btn.success:hover{box-shadow:0 4px 14px rgba(16,185,129,.4)}
.btn.warning{background:linear-gradient(135deg,#F59E0B,#D97706)}
.btn.warning:hover{box-shadow:0 4px 14px rgba(245,158,11,.4)}
.btn.purple{background:linear-gradient(135deg,#8B5CF6,#6D28D9)}
.btn.purple:hover{box-shadow:0 4px 14px rgba(139,92,246,.4)}
.btn.danger{background:linear-gradient(135deg,#EF4444,#DC2626)}
.btn.danger:hover{box-shadow:0 4px 14px rgba(239,68,68,.4)}
.btn.outline{background:transparent;border:1.5px solid #0EA5E9;color:#0369A1}
.btn.outline:hover{background:#F0F9FF;box-shadow:none}
.btn[disabled]{opacity:.45;cursor:not-allowed;transform:none!important;box-shadow:none!important}

/* Option cards (pickup / payment) */
.opt-card{border:2px solid #E2E8F0;border-radius:12px;padding:14px 16px;cursor:pointer;transition:all .2s;display:flex;align-items:center;gap:12px;background:#fff}
.opt-card:hover{border-color:#7DD3FC;background:#F0F9FF}
.opt-card.selected{border-color:#0EA5E9;background:#F0F9FF}
.opt-dot{width:18px;height:18px;border-radius:50%;border:2px solid #CBD5E1;margin-left:auto;flex-shrink:0;display:flex;align-items:center;justify-content:center;transition:all .2s}
.opt-card.selected .opt-dot{border-color:#0EA5E9;background:#0EA5E9}
.opt-card.selected .opt-dot::after{content:'';width:7px;height:7px;background:#fff;border-radius:50%;display:block}

/* Toast notification */
.toast{position:fixed;top:80px;right:24px;padding:13px 20px;border-radius:12px;z-index:9999;font-weight:700;font-size:14px;box-shadow:0 4px 20px rgba(0,0,0,.15);transform:translateX(420px);transition:transform .3s ease;max-width:340px;color:#fff}
.toast.show{transform:translateX(0)}
.toast.success{background:#10B981}
.toast.error{background:#EF4444}
.toast.info{background:#0EA5E9}

/* Modal */
.modal-bg{position:fixed;inset:0;background:rgba(15,23,42,.6);z-index:2000;display:flex;align-items:center;justify-content:center;padding:20px;backdrop-filter:blur(4px)}
.modal-box{background:#fff;border-radius:20px;padding:28px;width:100%;max-width:500px;max-height:90vh;overflow-y:auto;animation:modalIn .25s ease}
@keyframes modalIn{from{opacity:0;transform:scale(.95) translateY(10px)}to{opacity:1;transform:scale(1) translateY(0)}}
.modal-title{font-size:18px;font-weight:800;color:#0F172A;margin-bottom:4px}
.modal-sub{font-size:13px;color:#64748B;margin-bottom:20px}

/* Status badges */
.s-timbang{background:#FEF3C7;color:#92400E}
.s-bayar   {background:#EDE9FE;color:#5B21B6}
.s-proses  {background:#DBEAFE;color:#1E40AF}
.s-selesai {background:#D1FAE5;color:#065F46}
.s-done    {background:#F1F5F9;color:#475569}

/* Weight highlight */
.weight-box{background:linear-gradient(135deg,#FEF3C7,#FDE68A);border:1.5px dashed #FCD34D;border-radius:12px;padding:14px 18px;display:flex;align-items:center;gap:12px}

/* Notification bell badge */
.bell-wrap{position:relative;display:inline-flex}
.bell-badge{position:absolute;top:-4px;right:-4px;background:#EF4444;color:#fff;font-size:10px;font-weight:800;width:16px;height:16px;border-radius:50%;display:flex;align-items:center;justify-content:center;border:2px solid #fff}

/* ═══ NEW: Star Rating ═══ */
.star-selector{display:flex;gap:6px;justify-content:center;margin:12px 0}
.star-btn{font-size:36px;cursor:pointer;transition:transform .15s;background:none;border:none;line-height:1;padding:2px}
.star-btn:hover{transform:scale(1.2)}
.star-filled{color:#F59E0B}
.star-empty{color:#E2E8F0}
.stars-display{display:inline-flex;gap:2px;align-items:center}
.stars-display span{font-size:14px}

/* ═══ NEW: Inventory / Stock ═══ */
.stock-ok    {background:#D1FAE5;color:#065F46}
.stock-warn  {background:#FEF3C7;color:#92400E}
.stock-low   {background:#FEE2E2;color:#991B1B}
.inv-card{background:#fff;border-radius:14px;padding:18px;box-shadow:0 1px 6px rgba(0,0,0,.06);border-left:4px solid #E2E8F0;margin-bottom:10px;display:flex;align-items:center;gap:14px;transition:box-shadow .2s}
.inv-card:hover{box-shadow:0 4px 16px rgba(0,0,0,.1)}
.inv-icon{font-size:28px;width:44px;text-align:center;flex-shrink:0}
.inv-info{flex:1;min-width:0}
.inv-name{font-size:15px;font-weight:800;color:#0F172A}
.inv-meta{font-size:12px;color:#64748B;margin-top:3px}
.inv-stock-bar{height:6px;border-radius:99px;background:#F1F5F9;margin-top:6px;overflow:hidden}
.inv-stock-fill{height:6px;border-radius:99px;transition:width .4s}
.alert-banner{background:#FEE2E2;border:1.5px solid #FCA5A5;border-radius:12px;padding:12px 16px;font-size:13px;font-weight:700;color:#991B1B;margin-bottom:16px;display:flex;align-items:center;gap:10px}

/* ═══ NEW: Review Card ═══ */
.review-card{background:#F8FAFC;border-radius:14px;padding:16px;margin-bottom:12px;border:1.5px solid #F1F5F9}
.review-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;flex-wrap:wrap;gap:6px}
.review-name{font-weight:700;font-size:14px;color:#0F172A}
.review-date{font-size:12px;color:#94A3B8}
.review-comment{font-size:14px;color:#374151;line-height:1.6;margin-top:6px}

/* ═══════════════════════════════════════════════════════════
   CUSTOMER APP
═══════════════════════════════════════════════════════════ */
.c-app{min-height:100vh;background:#F0F9FF}
.c-header{background:linear-gradient(135deg,#0EA5E9 0%,#0284C7 50%,#0369A1 100%);padding:0 24px;display:flex;align-items:center;justify-content:space-between;height:64px;box-shadow:0 4px 20px rgba(14,165,233,.3);position:sticky;top:0;z-index:100}
.c-logo{color:#fff;font-weight:900;font-size:22px;letter-spacing:-.5px;display:flex;align-items:center;gap:8px;cursor:pointer}
.c-nav{display:flex;gap:4px;align-items:center}
.c-nav-btn{background:transparent;border:none;color:#fff;padding:8px 14px;border-radius:10px;cursor:pointer;font-family:inherit;font-size:13px;font-weight:600;display:flex;align-items:center;gap:5px;transition:all .2s}
.c-nav-btn:hover,.c-nav-btn.active{background:rgba(255,255,255,.25)}
.c-content{max-width:1100px;margin:0 auto;padding:32px 20px}
.hero{background:linear-gradient(135deg,#0EA5E9,#0369A1);border-radius:20px;padding:48px 40px;color:#fff;margin-bottom:28px;position:relative;overflow:hidden}
.hero h1{font-size:38px;font-weight:900;margin:0 0 12px;line-height:1.2}

/* Queue badge on order card */
.queue-pill{background:rgba(255,255,255,.25);color:#fff;font-weight:800;padding:4px 14px;border-radius:99px;font-size:13px;display:inline-flex;align-items:center;gap:6px}

/* ═══════════════════════════════════════════════════════════
   STAFF APP
═══════════════════════════════════════════════════════════ */
.s-app{display:flex;min-height:100vh;background:#F1F5F9}
.s-sidebar{width:240px;background:#1E293B;display:flex;flex-direction:column;position:fixed;top:0;left:0;height:100vh;z-index:50;transition:transform .3s}
.s-brand{padding:20px 24px;border-bottom:1px solid rgba(255,255,255,.08)}
.s-brand-name{color:#fff;font-weight:900;font-size:18px}
.s-brand-sub{color:#64748B;font-size:11px;font-weight:600;letter-spacing:1px;text-transform:uppercase;margin-top:2px}
.s-nav-section{padding:16px 12px 8px;color:#475569;font-size:11px;font-weight:700;letter-spacing:1px;text-transform:uppercase}
.s-nav-item{display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:10px;cursor:pointer;color:#94A3B8;font-size:14px;font-weight:600;transition:all .2s;margin:2px 8px;text-decoration:none}
.s-nav-item:hover{background:rgba(255,255,255,.06);color:#E2E8F0}
.s-nav-item.active{background:rgba(14,165,233,.2);color:#38BDF8}
.s-nav-item .s-nav-icon{font-size:17px;width:22px;text-align:center}
.s-badge-pill{background:#EF4444;color:#fff;font-size:10px;font-weight:800;padding:1px 6px;border-radius:99px;margin-left:auto}
.s-badge-warn{background:#F59E0B;color:#fff;font-size:10px;font-weight:800;padding:1px 6px;border-radius:99px;margin-left:auto}
.s-main{margin-left:240px;flex:1;display:flex;flex-direction:column;min-height:100vh}
.s-topbar{background:#fff;border-bottom:1px solid #E2E8F0;padding:0 28px;height:60px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:40}
.s-topbar-title{font-size:17px;font-weight:800;color:#0F172A}
.s-topbar-right{display:flex;align-items:center;gap:14px}
.s-staff-info{display:flex;align-items:center;gap:8px}
.s-avatar{width:34px;height:34px;background:linear-gradient(135deg,#0EA5E9,#0369A1);border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:800;font-size:13px}
.s-content{padding:28px;flex:1}

/* Staff stat cards */
.stat-card{background:#fff;border-radius:14px;padding:20px;box-shadow:0 1px 6px rgba(0,0,0,.06);display:flex;align-items:center;gap:16px}
.stat-icon{width:48px;height:48px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:22px;flex-shrink:0}
.stat-val{font-size:28px;font-weight:900;line-height:1}
.stat-label{font-size:13px;color:#64748B;margin-top:3px;font-weight:600}

/* Queue card in staff */
.queue-card{background:#fff;border-radius:14px;padding:18px 20px;box-shadow:0 1px 6px rgba(0,0,0,.05);border-left:4px solid #E2E8F0;margin-bottom:12px;display:flex;align-items:center;gap:16px;transition:box-shadow .2s}
.queue-card:hover{box-shadow:0 4px 16px rgba(0,0,0,.1)}
.queue-num{font-size:22px;font-weight:900;color:#0369A1;min-width:80px}
.queue-info{flex:1}
.queue-name{font-size:15px;font-weight:800;color:#0F172A}
.queue-meta{font-size:13px;color:#64748B;margin-top:3px}
.queue-actions{display:flex;gap:8px;flex-wrap:wrap}

/* ═══════════════════════════════════════════════════════════
   RESPONSIVE
═══════════════════════════════════════════════════════════ */
@media(max-width:900px){
  .grid2,.grid3,.grid4{grid-template-columns:1fr}
  .hero{padding:32px 24px}
  .hero h1{font-size:26px}
  .s-sidebar{transform:translateX(-100%)}
  .s-main{margin-left:0}
  .order-cols{grid-template-columns:1fr!important}
}
</style>
</head>
<body>
<div id="app"></div>
<div id="modal-container"></div>
<div id="toast" class="toast hidden"></div>

<script>
// ═══════════════════════════════════════════════════════════
// CONSTANTS
// ═══════════════════════════════════════════════════════════
const SERVICES = [
  {id:'cuci-setrika', name:'Cuci & Setrika',  price:10000, hours:24, icon:'👕', desc:'Dicuci bersih + disetrika rapi'},
  {id:'cuci-kering',  name:'Cuci Kering',     price:8000,  hours:18, icon:'🌀', desc:'Dicuci + dikeringkan mesin'},
  {id:'setrika-saja', name:'Setrika Saja',    price:7000,  hours:12, icon:'♨️', desc:'Hanya layanan setrika'},
  {id:'express',      name:'Express (6 jam)', price:15000, hours:6,  icon:'⚡', desc:'Selesai dalam 6 jam, cuci + setrika'},
];
const PICKUP_OPTS = [
  {id:'antar-mandiri', icon:'🏪', title:'Antar Mandiri ke Outlet', desc:'Bawa langsung ke outlet kami'},
  {id:'dijemput',      icon:'🛵', title:'Dijemput ke Alamat',      desc:'Kurir kami jemput (+Rp 5.000)'},
];
const PAYMENT_OPTS = [
  {id:'cash',     icon:'💵', title:'Tunai (Cash)',   desc:'Bayar di outlet / ke kurir'},
  {id:'transfer', icon:'🏦', title:'Transfer Bank',  desc:'BCA / Mandiri / BNI / BRI'},
  {id:'qris',     icon:'📱', title:'QRIS',           desc:'Scan QR — semua e-wallet'},
];
const REWARDS = [
  {id:1, name:'Diskon 10%',      pts:100, icon:'🏷️', desc:'Diskon 10% untuk transaksi berikutnya'},
  {id:2, name:'Gratis Cuci 2kg', pts:250, icon:'👕', desc:'Gratis cuci hingga 2kg'},
  {id:3, name:'Gratis Setrika',  pts:150, icon:'🔥', desc:'Gratis setrika satu order'},
  {id:4, name:'Diskon 25%',      pts:400, icon:'💎', desc:'Diskon besar 25%'},
  {id:5, name:'Gratis Cuci 5kg', pts:600, icon:'🎁', desc:'Gratis cuci hingga 5kg'},
];
const DETERGENTS = ['Attack','Rinso Anti Noda','Daia Bunga','So Klin'];
const MACHINES   = ['Mesin LG 9kg','Mesin Samsung 10kg','Setrika Uap Philips'];
const STAFF_ACCOUNTS = [
  {id:'s1', username:'admin',     password:'cleanwave123', name:'Admin',   role:'admin'},
  {id:'s2', username:'karyawan1', password:'karyawan123',  name:'Rizky',   role:'staff'},
  {id:'s3', username:'karyawan2', password:'karyawan123',  name:'Dewi',    role:'staff'},
];

const STATUS_CFG = {
  'menunggu-timbang':{ label:'Menunggu Timbang', cls:'s-timbang', icon:'⚖️' },
  'menunggu-bayar':  { label:'Menunggu Bayar',   cls:'s-bayar',   icon:'💳' },
  'diproses':        { label:'Sedang Diproses',  cls:'s-proses',  icon:'🫧' },
  'selesai':         { label:'Siap Diambil',     cls:'s-selesai', icon:'✅' },
  'selesai-bayar':   { label:'Selesai',          cls:'s-done',    icon:'📦' },
};

// ═══ NEW: Inventaris default data ═══
const DEFAULT_INVENTORY = [
  // Deterjen
  {id:'inv1', cat:'Deterjen',   name:'Attack',           unit:'kg',     stock:15, minStock:3,  icon:'🧴', price:25000},
  {id:'inv2', cat:'Deterjen',   name:'Rinso Anti Noda',  unit:'kg',     stock:8,  minStock:3,  icon:'🧴', price:28000},
  {id:'inv3', cat:'Deterjen',   name:'Daia Bunga',       unit:'kg',     stock:12, minStock:3,  icon:'🧴', price:20000},
  {id:'inv4', cat:'Deterjen',   name:'So Klin',          unit:'kg',     stock:2,  minStock:3,  icon:'🧴', price:22000},
  // Pelembut & Pewangi
  {id:'inv5', cat:'Pelembut',   name:'Molto Ungu',       unit:'liter',  stock:4,  minStock:2,  icon:'💧', price:18000},
  {id:'inv6', cat:'Pelembut',   name:'Downy Sunrise',    unit:'liter',  stock:1,  minStock:2,  icon:'💧', price:20000},
  {id:'inv7', cat:'Pelembut',   name:'Molto Putih Bersih',unit:'liter', stock:5,  minStock:2,  icon:'💧', price:17000},
  // Peralatan
  {id:'inv8', cat:'Peralatan',  name:'Hanger Kawat',     unit:'buah',   stock:80, minStock:20, icon:'🪝', price:1500},
  {id:'inv9', cat:'Peralatan',  name:'Plastik Kemasan',  unit:'lembar', stock:200,minStock:50, icon:'📦', price:500},
  {id:'inv10',cat:'Peralatan',  name:'Label Pesanan',    unit:'lembar', stock:45, minStock:30, icon:'🏷️', price:200},
  {id:'inv11',cat:'Peralatan',  name:'Kantong Laundry',  unit:'buah',   stock:60, minStock:20, icon:'🛍️', price:2000},
  // Mesin & Alat Besar
  {id:'inv12',cat:'Mesin',      name:'Mesin LG 9kg',     unit:'unit',   stock:1,  minStock:1,  icon:'🌀', price:0, status:'Aktif',        lastMaint:'2025-03-01'},
  {id:'inv13',cat:'Mesin',      name:'Mesin Samsung 10kg',unit:'unit',  stock:1,  minStock:1,  icon:'🌀', price:0, status:'Aktif',        lastMaint:'2025-02-15'},
  {id:'inv14',cat:'Mesin',      name:'Setrika Uap Philips',unit:'unit', stock:2,  minStock:1,  icon:'♨️', price:0, status:'Aktif',        lastMaint:'2025-01-20'},
  {id:'inv15',cat:'Mesin',      name:'Mesin Pengering LG',unit:'unit',  stock:1,  minStock:1,  icon:'🌬️', price:0, status:'Maintenance',  lastMaint:'2025-04-10'},
];

// ═══════════════════════════════════════════════════════════
// STATE
// ═══════════════════════════════════════════════════════════
let S = {
  mode:'customer',
  page:'home',
  staffPage:'dashboard',
  loggedIn:null,
  staffAuth:null,
  customers:[
    {id:1, name:'Budi Santoso',  phone:'081234567890', email:'budi@email.com',  joinDate:'2024-01-10', pts:320, tier:'Silver'},
    {id:2, name:'Siti Rahayu',   phone:'082345678901', email:'siti@email.com',  joinDate:'2024-02-15', pts:750, tier:'Gold'},
    {id:3, name:'Ahmad Fauzi',   phone:'083456789012', email:'ahmad@email.com', joinDate:'2024-03-20', pts:120, tier:'Bronze'},
  ],
  transactions:[
    {id:101, customerId:1, qNum:'CW-001', date:'2025-04-01', kg:3.5, serviceId:'cuci-setrika', service:'Cuci & Setrika', price:35000, status:'selesai-bayar', pts:35, detergent:'Attack',  machine:'Mesin LG 9kg',       pickupMethod:'antar-mandiri', paymentMethod:'cash',     address:'', notes:'', estimatedDone:'2025-04-02T17:00:00', paidAt:'2025-04-02', notified:true},
    {id:102, customerId:2, qNum:'CW-002', date:'2025-04-05', kg:5.0, serviceId:'cuci-kering',  service:'Cuci Kering',   price:40000, status:'selesai-bayar', pts:40, detergent:'Rinso',   machine:'Mesin Samsung 10kg', pickupMethod:'dijemput',      paymentMethod:'transfer', address:'Jl. Mawar No. 12', notes:'', estimatedDone:'2025-04-06T11:00:00', paidAt:'2025-04-06', notified:true},
    {id:103, customerId:1, qNum:'CW-003', date:'2025-04-10', kg:2.0, serviceId:'setrika-saja', service:'Setrika Saja',  price:14000, status:'selesai',      pts:14, detergent:'-',       machine:'Setrika Uap Philips', pickupMethod:'antar-mandiri', paymentMethod:'qris',     address:'', notes:'', estimatedDone:'2025-04-10T22:00:00', paidAt:null, notified:true},
    {id:104, customerId:3, qNum:'CW-004', date:'2025-04-12', kg:4.0, serviceId:'cuci-setrika', service:'Cuci & Setrika', price:40000, status:'diproses',    pts:40, detergent:'Daia',    machine:'Mesin LG 9kg',       pickupMethod:'dijemput',      paymentMethod:'cash',     address:'Jl. Anggrek No. 5', notes:'', estimatedDone:'2025-04-13T14:00:00', paidAt:'2025-04-12', notified:false},
    {id:105, customerId:2, qNum:'CW-005', date:'2025-04-15', kg:null,serviceId:'cuci-kering',  service:'Cuci Kering',   price:null,  status:'menunggu-timbang', pts:0, detergent:null, machine:null, pickupMethod:'antar-mandiri', paymentMethod:'transfer', address:'', notes:'', estimatedDone:null, paidAt:null, notified:false},
  ],
  notifications:[
    {id:'n1', customerId:1, txId:103, type:'order-done', msg:'Laundry Anda #CW-003 sudah selesai dan siap diambil! 🎉', read:false, createdAt:'2025-04-10T22:05:00'},
    {id:'n2', customerId:3, txId:104, type:'processing',  msg:'Laundry #CW-004 sedang dalam proses pencucian. Estimasi selesai: Minggu 13 Apr pukul 14.00', read:false, createdAt:'2025-04-12T10:00:00'},
  ],
  // ═══ NEW: Ratings ═══
  ratings:[
    {id:'r1', customerId:1, txId:101, stars:5, comment:'Baju bersih banget dan wangi! Pelayanannya juga ramah, pasti balik lagi.', createdAt:'2025-04-02T20:00:00'},
    {id:'r2', customerId:2, txId:102, stars:4, comment:'Hasil cucian oke dan pengiriman tepat waktu. Lumayan puas!', createdAt:'2025-04-06T15:00:00'},
  ],
  // ═══ NEW: Inventory ═══
  inventory: JSON.parse(JSON.stringify(DEFAULT_INVENTORY)),
  // ═══ NEW: Forms ═══
  ratingForm:{stars:0, comment:''},
  invFilter:'Semua',
  antriFilter:'Semua',
  qCounter:5,
  modal:null,
  orderForm:{name:'',phone:'',address:'',serviceId:'cuci-setrika',pickupMethod:'antar-mandiri',paymentMethod:'cash',notes:''},
  orderDone:false, orderTx:null,
  loginForm:{phone:''},
  loginTab:'login',
  regForm:{name:'',phone:'',email:''},
  staffLoginForm:{username:'',password:''},
  historySearch:'', historyFilter:'Semua',
  checkStatusQuery:'',checkStatusResult:null,
};

// ═══════════════════════════════════════════════════════════
// PERSIST
// ═══════════════════════════════════════════════════════════
function save(){
  localStorage.setItem('cw_state', JSON.stringify({
    customers:S.customers, transactions:S.transactions,
    notifications:S.notifications, qCounter:S.qCounter,
    loggedIn:S.loggedIn, staffAuth:S.staffAuth, mode:S.mode,
    ratings:S.ratings, inventory:S.inventory,
  }));
}
function load(){
  try{
    const d = JSON.parse(localStorage.getItem('cw_state')||'{}');
    if(d.customers)     S.customers     = d.customers;
    if(d.transactions)  S.transactions  = d.transactions;
    if(d.notifications) S.notifications = d.notifications;
    if(d.qCounter)      S.qCounter      = d.qCounter;
    if(d.loggedIn)      S.loggedIn      = d.loggedIn;
    if(d.staffAuth)     S.staffAuth     = d.staffAuth;
    if(d.mode)          S.mode          = d.mode;
    if(d.ratings)       S.ratings       = d.ratings;
    if(d.inventory)     S.inventory     = d.inventory;
    if(S.mode==='staff' && S.staffAuth) S.page = 'home';
  }catch(e){}
}

// ═══════════════════════════════════════════════════════════
// UTILS
// ═══════════════════════════════════════════════════════════
function getTier(pts){
  if(pts>=500) return {name:'Gold',  color:'#D97706', bg:'#FEF3C7'};
  if(pts>=200) return {name:'Silver',color:'#6B7280', bg:'#F3F4F6'};
  return {name:'Bronze',color:'#92400E',bg:'#FEF9C3'};
}
function rp(n){ return 'Rp '+(n||0).toLocaleString('id'); }
function nextQueue(){
  S.qCounter++;
  return 'CW-'+String(S.qCounter).padStart(3,'0');
}
function calcEstimated(serviceId, ahead=0){
  const svc = SERVICES.find(s=>s.id===serviceId)||SERVICES[0];
  const extra = ahead * 1.5;
  const d = new Date(Date.now() + (svc.hours + extra)*3600000);
  return d.toISOString();
}
function fmtEst(iso){
  if(!iso) return '—';
  const d=new Date(iso), now=new Date();
  const tom=new Date(now); tom.setDate(tom.getDate()+1);
  const days=['Minggu','Senin','Selasa','Rabu','Kamis','Jumat','Sabtu'];
  const months=['Jan','Feb','Mar','Apr','Mei','Jun','Jul','Agt','Sep','Okt','Nov','Des'];
  let day;
  if(d.toDateString()===now.toDateString()) day='Hari ini';
  else if(d.toDateString()===tom.toDateString()) day='Besok';
  else day=`${days[d.getDay()]}, ${d.getDate()} ${months[d.getMonth()]}`;
  return `${day} pukul ${String(d.getHours()).padStart(2,'0')}.${String(d.getMinutes()).padStart(2,'0')}`;
}
function statusBadge(status){
  const c=STATUS_CFG[status]||{label:status,cls:'s-timbang',icon:'?'};
  return `<span class="badge ${c.cls}">${c.icon} ${c.label}</span>`;
}
function payLbl(id){ return {cash:'💵 Tunai',transfer:'🏦 Transfer',qris:'📱 QRIS'}[id]||id; }
function pickLbl(id){ return {dijemput:'🛵 Dijemput','antar-mandiri':'🏪 Mandiri'}[id]||id; }
function unreadCount(custId){ return S.notifications.filter(n=>n.customerId===custId&&!n.read).length; }
function addNotif(custId, txId, type, msg){
  S.notifications.push({id:'n'+Date.now(),customerId:custId,txId,type,msg,read:false,createdAt:new Date().toISOString()});
}

// ═══ NEW UTILS ═══
function renderStars(n, size=16){
  return [1,2,3,4,5].map(i=>`<span style="font-size:${size}px;color:${i<=n?'#F59E0B':'#D1D5DB'};">★</span>`).join('');
}
function avgRating(){
  if(!S.ratings.length) return 0;
  return (S.ratings.reduce((s,r)=>s+r.stars,0)/S.ratings.length).toFixed(1);
}
function getStockStatus(item){
  if(item.cat==='Mesin') return item.status==='Aktif' ? 'ok' : item.status==='Maintenance' ? 'warn' : 'low';
  const pct = item.stock / item.minStock;
  if(pct >= 2) return 'ok';
  if(pct >= 1) return 'warn';
  return 'low';
}
function stockBadge(item){
  const st=getStockStatus(item);
  const cfg={ok:{cls:'stock-ok',lbl:'Cukup'},warn:{cls:'stock-warn',lbl:'Hampir Habis'},low:{cls:'stock-low',lbl:'Stok Menipis'}};
  if(item.cat==='Mesin'){
    const sc={Aktif:{cls:'stock-ok'},Maintenance:{cls:'stock-warn'},Rusak:{cls:'stock-low'}};
    return `<span class="badge ${sc[item.status]?.cls||'stock-ok'}">${item.status||'Aktif'}</span>`;
  }
  return `<span class="badge ${cfg[st].cls}">${cfg[st].lbl} (${item.stock} ${item.unit})</span>`;
}
function lowStockCount(){
  return S.inventory.filter(i=>{
    if(i.cat==='Mesin') return i.status && i.status!=='Aktif';
    return i.stock < i.minStock;
  }).length;
}
function maskName(name){
  if(!name) return 'Pelanggan';
  const parts = name.split(' ');
  return parts[0] + (parts.length>1?' '+parts[1][0]+'.':'');
}

// Toast
let toastTimer;
function toast(msg, type='success'){
  const el=document.getElementById('toast');
  el.textContent=({success:'✅ ',error:'❌ ',info:'💬 '}[type]||'')+msg;
  el.className=`toast ${type} show`;
  clearTimeout(toastTimer);
  toastTimer=setTimeout(()=>el.classList.remove('show'),3500);
}

// ═══════════════════════════════════════════════════════════
// MODAL ENGINE
// ═══════════════════════════════════════════════════════════
function openModal(type, data={}){ S.modal={type,data}; renderModal(); }
function closeModal(){ S.modal=null; document.getElementById('modal-container').innerHTML=''; }

function renderModal(){
  const mc=document.getElementById('modal-container');
  if(!S.modal){ mc.innerHTML=''; return; }
  const {type,data}=S.modal;
  let body='';
  if(type==='input-berat')    body=modalInputBerat(data);
  if(type==='konfirm-bayar')  body=modalKonfirmBayar(data);
  if(type==='wa-notif')       body=modalWaNotif(data);
  if(type==='update-status')  body=modalUpdateStatus(data);
  if(type==='notif-list')     body=modalNotifList(data);
  if(type==='invoice')        body=modalInvoice(data);
  if(type==='rating')         body=modalRating(data);          // NEW
  if(type==='inv-edit')       body=modalInvEdit(data);         // NEW

  mc.innerHTML=`
    <div class="modal-bg" onclick="bgClose(event)">
      <div class="modal-box">${body}</div>
    </div>`;
}
function bgClose(e){ if(e.target.classList.contains('modal-bg')) closeModal(); }

// ─── Modal: Input Berat ────────────────────────────────────
function modalInputBerat({txId}){
  const tx=S.transactions.find(t=>t.id===txId);
  const cust=S.customers.find(c=>c.id===tx.customerId);
  const svc=SERVICES.find(s=>s.id===tx.serviceId)||SERVICES[0];
  const activeQ=S.transactions.filter(t=>['menunggu-timbang','menunggu-bayar','diproses'].includes(t.status)).length;
  const defEst=calcEstimated(tx.serviceId, activeQ);
  const surcharge=tx.pickupMethod==='dijemput'?5000:0;

  // Only show active/available detergents from inventory
  const availDet = S.inventory.filter(i=>i.cat==='Deterjen' && i.stock>0).map(i=>i.name);
  const detOptions = availDet.length > 0 ? availDet : DETERGENTS;
  const availMach = S.inventory.filter(i=>i.cat==='Mesin' && (i.status==='Aktif'||!i.status)).map(i=>i.name);
  const machOptions = availMach.length > 0 ? availMach : MACHINES;

  return `
    <div>
      <div class="modal-title">⚖️ Input Berat Laundry</div>
      <div class="modal-sub">Order ${tx.qNum} · ${cust?.name}</div>

      <div style="background:#F0F9FF;border-radius:12px;padding:14px;margin-bottom:20px;font-size:13px;">
        <div style="display:flex;gap:20px;flex-wrap:wrap;">
          <span><strong>Layanan:</strong> ${tx.service}</span>
          <span><strong>Metode:</strong> ${pickLbl(tx.pickupMethod)}</span>
          <span><strong>Bayar:</strong> ${payLbl(tx.paymentMethod)}</span>
        </div>
        ${tx.notes?`<div style="margin-top:6px;color:#64748B;">📝 ${tx.notes}</div>`:''}
      </div>

      <div class="mb14">
        <label class="label">Berat Laundry (kg)</label>
        <input class="input" id="m-kg" type="number" min="0.5" max="30" step="0.5" placeholder="Contoh: 3.5" />
      </div>
      <div class="mb14">
        <label class="label">Deterjen yang Digunakan</label>
        <select class="input" id="m-det">
          ${detOptions.map(d=>`<option>${d}</option>`).join('')}
        </select>
      </div>
      <div class="mb14">
        <label class="label">Mesin yang Digunakan</label>
        <select class="input" id="m-mach">
          ${machOptions.map(m=>`<option>${m}</option>`).join('')}
        </select>
      </div>
      <div class="mb14">
        <label class="label">Estimasi Selesai</label>
        <input class="input" id="m-est" type="datetime-local" value="${defEst.slice(0,16)}" />
      </div>

      <div id="m-preview" style="background:#F8FAFC;border-radius:10px;padding:14px;margin-bottom:18px;display:none;">
        <div style="font-size:12px;color:#64748B;font-weight:700;margin-bottom:8px;">PREVIEW INVOICE</div>
        <div style="display:flex;justify-content:space-between;font-size:14px;margin-bottom:6px;">
          <span>Harga Cuci (<span id="pv-kg">0</span> kg × <span id="pv-rate">${rp(svc.price)}</span>)</span>
          <span id="pv-sub" style="font-weight:700;"></span>
        </div>
        ${surcharge>0?`<div style="display:flex;justify-content:space-between;font-size:14px;margin-bottom:6px;"><span>Biaya Jemput</span><span style="font-weight:700;">${rp(surcharge)}</span></div>`:''}
        <hr class="divider">
        <div style="display:flex;justify-content:space-between;font-size:16px;font-weight:900;">
          <span>Total</span><span style="color:#0369A1;" id="pv-total"></span>
        </div>
        <div style="font-size:12px;color:#D97706;margin-top:8px;" id="pv-pts"></div>
      </div>

      <div style="display:flex;gap:10px;justify-content:flex-end;">
        <button class="btn secondary" onclick="closeModal()">Batal</button>
        <button class="btn success" onclick="doInputBerat(${txId},${surcharge},${svc.price})">💾 Simpan & Kirim Invoice</button>
      </div>
    </div>
    <script>
      (function(){
        const kgEl=document.getElementById('m-kg');
        const prev=document.getElementById('m-preview');
        kgEl.addEventListener('input',function(){
          const kg=parseFloat(this.value)||0;
          if(kg>0){
            const sub=Math.ceil(kg*${svc.price});
            const tot=sub+${surcharge};
            document.getElementById('pv-kg').textContent=kg;
            document.getElementById('pv-sub').textContent='Rp '+sub.toLocaleString('id');
            document.getElementById('pv-total').textContent='Rp '+tot.toLocaleString('id');
            document.getElementById('pv-pts').textContent='⭐ Poin yang akan didapat: '+Math.floor(tot/1000)+' poin';
            prev.style.display='block';
          } else { prev.style.display='none'; }
        });
      })();
    <\/script>
  `;
}

// ─── Modal: Konfirmasi Bayar ───────────────────────────────
function modalKonfirmBayar({txId}){
  const tx=S.transactions.find(t=>t.id===txId);
  const cust=S.customers.find(c=>c.id===tx.customerId);
  return `
    <div>
      <div class="modal-title">💳 Konfirmasi Pembayaran</div>
      <div class="modal-sub">Order ${tx.qNum} · ${cust?.name}</div>
      <div style="background:#F0F9FF;border-radius:14px;padding:18px;margin-bottom:20px;">
        ${[
          ['Layanan', tx.service],
          ['Berat',   tx.kg+' kg'],
          ['Metode Bayar', payLbl(tx.paymentMethod)],
        ].map(([k,v])=>`
          <div style="display:flex;justify-content:space-between;margin-bottom:8px;font-size:14px;">
            <span style="color:#64748B;">${k}</span><strong>${v}</strong>
          </div>`).join('')}
        <hr class="divider">
        <div style="display:flex;justify-content:space-between;font-size:20px;font-weight:900;">
          <span>Total</span><span style="color:#0369A1;">${rp(tx.price)}</span>
        </div>
      </div>
      <div class="mb16">
        <label class="label">Catatan Pembayaran (opsional)</label>
        <input class="input" id="m-pay-note" placeholder="No. referensi transfer, dll." />
      </div>
      <div style="display:flex;gap:10px;justify-content:flex-end;">
        <button class="btn secondary" onclick="closeModal()">Batal</button>
        <button class="btn success" onclick="doKonfirmBayar(${txId})">✅ Konfirmasi Lunas</button>
      </div>
    </div>`;
}

// ─── Modal: WA Notification ────────────────────────────────
function modalWaNotif({txId, msg, custPhone}){
  return `
    <div style="text-align:center;">
      <div style="font-size:56px;margin-bottom:12px;">📱</div>
      <div class="modal-title" style="text-align:center;">Simulasi Notifikasi WhatsApp</div>
      <div class="modal-sub" style="text-align:center;margin-bottom:20px;">Pesan berikut akan dikirim ke ${custPhone}</div>
      <div style="background:#DCF8C6;border-radius:12px;padding:16px;text-align:left;margin-bottom:20px;border-radius:0 12px 12px 12px;position:relative;">
        <div style="font-size:14px;line-height:1.6;color:#0F172A;white-space:pre-line;">${msg}</div>
        <div style="font-size:11px;color:#64748B;text-align:right;margin-top:8px;">✓✓ Terkirim</div>
      </div>
      <div style="background:#E7F8EE;border-radius:10px;padding:12px;margin-bottom:20px;font-size:13px;color:#065F46;font-weight:600;">
        ✅ Notifikasi berhasil dikirim ke WhatsApp ${custPhone}
      </div>
      <button class="btn block" onclick="closeModal()">Tutup</button>
    </div>`;
}

// ─── Modal: Update Status ──────────────────────────────────
function modalUpdateStatus({txId}){
  const tx=S.transactions.find(t=>t.id===txId);
  const opts=[
    {val:'diproses',       label:'Sedang Diproses 🫧'},
    {val:'selesai',        label:'Siap Diambil ✅'},
    {val:'selesai-bayar',  label:'Selesai & Sudah Diambil 📦'},
  ].filter(o=>o.val!==tx.status);
  return `
    <div>
      <div class="modal-title">🔄 Update Status</div>
      <div class="modal-sub">Order ${tx.qNum} — status saat ini: ${STATUS_CFG[tx.status]?.label||tx.status}</div>
      <div style="display:flex;flex-direction:column;gap:10px;margin-bottom:20px;">
        ${opts.map(o=>`
          <button class="btn block secondary" style="justify-content:flex-start;padding:14px 18px;" onclick="doUpdateStatus(${txId},'${o.val}')">
            ${o.label}
          </button>`).join('')}
      </div>
      <button class="btn secondary block" onclick="closeModal()">Batal</button>
    </div>`;
}

// ─── Modal: Notification List ──────────────────────────────
function modalNotifList({custId}){
  const notifs=S.notifications.filter(n=>n.customerId===custId).sort((a,b)=>b.id.localeCompare(a.id));
  S.notifications.forEach(n=>{if(n.customerId===custId) n.read=true;});
  save();
  return `
    <div>
      <div class="modal-title">🔔 Notifikasi</div>
      <div class="modal-sub">${notifs.length} notifikasi</div>
      ${notifs.length===0?`<div style="text-align:center;color:#94A3B8;padding:32px;">Belum ada notifikasi</div>`:
        notifs.map(n=>`
          <div style="border:1.5px solid #E2E8F0;border-radius:12px;padding:14px;margin-bottom:10px;">
            <div style="font-size:14px;color:#0F172A;margin-bottom:4px;">${n.msg}</div>
            <div style="font-size:12px;color:#94A3B8;">${fmtEst(n.createdAt)}</div>
          </div>`).join('')}
      <button class="btn block secondary" style="margin-top:8px;" onclick="closeModal()">Tutup</button>
    </div>`;
}

// ─── Modal: Invoice ────────────────────────────────────────
function modalInvoice({txId}){
  const tx=S.transactions.find(t=>t.id===txId);
  const cust=S.customers.find(c=>c.id===tx.customerId);
  return `
    <div>
      <div style="text-align:center;margin-bottom:20px;">
        <div style="font-size:40px;margin-bottom:8px;">🧾</div>
        <div class="modal-title" style="text-align:center;">Invoice Laundry</div>
        <div class="modal-sub" style="text-align:center;">Order ${tx.qNum}</div>
      </div>
      <div style="background:#F0F9FF;border-radius:14px;padding:18px;margin-bottom:16px;">
        ${[
          ['Nama',          cust?.name||'-'],
          ['Layanan',       tx.service],
          ['Berat',         (tx.kg||'-')+' kg'],
          ['Deterjen',      tx.detergent||'-'],
          ['Pengambilan',   pickLbl(tx.pickupMethod)],
          ['Metode Bayar',  payLbl(tx.paymentMethod)],
          ['Estimasi Selesai', fmtEst(tx.estimatedDone)],
        ].map(([k,v])=>`
          <div style="display:flex;justify-content:space-between;margin-bottom:8px;font-size:13px;">
            <span style="color:#64748B;">${k}</span><strong style="text-align:right;max-width:60%;">${v}</strong>
          </div>`).join('')}
        <hr class="divider">
        <div style="display:flex;justify-content:space-between;font-size:18px;font-weight:900;">
          <span>Total</span><span style="color:#0369A1;">${tx.price!==null?rp(tx.price):'Dihitung setelah timbang'}</span>
        </div>
        ${tx.pts?`<div style="font-size:13px;color:#D97706;margin-top:8px;font-weight:600;">⭐ +${tx.pts} poin akan ditambahkan</div>`:''}
      </div>
      ${tx.status==='menunggu-bayar'?`
        <div style="background:#EDE9FE;border-radius:10px;padding:12px;margin-bottom:16px;font-size:13px;color:#5B21B6;font-weight:600;">
          💳 Silakan lunasi pembayaran di outlet atau tunjukkan halaman ini kepada karyawan.
        </div>`:''}
      <div style="text-align:center;">
        ${statusBadge(tx.status)}
      </div>
      <button class="btn block secondary" style="margin-top:16px;" onclick="closeModal()">Tutup</button>
    </div>`;
}

// ─── NEW Modal: Rating ────────────────────────────────────
function modalRating({txId}){
  const tx=S.transactions.find(t=>t.id===txId);
  const stars=S.ratingForm.stars;
  const labels=['','Sangat Buruk','Kurang Memuaskan','Cukup','Baik','Sangat Memuaskan! 🎉'];
  return `
    <div>
      <div style="text-align:center;margin-bottom:8px;">
        <div style="font-size:48px;margin-bottom:8px;">⭐</div>
        <div class="modal-title" style="text-align:center;">Beri Nilai Layanan</div>
        <div class="modal-sub" style="text-align:center;">Order ${tx?.qNum} · ${tx?.service}</div>
      </div>

      <div style="background:#FFFBEB;border-radius:12px;padding:18px;text-align:center;margin-bottom:20px;">
        <div style="font-size:13px;color:#92400E;font-weight:600;margin-bottom:12px;">Seberapa puas Anda dengan layanan kami?</div>
        <div class="star-selector" id="star-selector">
          ${[1,2,3,4,5].map(i=>`
            <button class="star-btn" onclick="selectStar(${i},${txId})">
              <span style="font-size:40px;color:${i<=stars?'#F59E0B':'#D1D5DB'};">★</span>
            </button>`).join('')}
        </div>
        <div style="font-size:15px;font-weight:800;color:${stars>0?'#D97706':'#94A3B8'};margin-top:8px;min-height:24px;">
          ${stars>0?labels[stars]:'Ketuk bintang untuk menilai'}
        </div>
      </div>

      <div class="mb14">
        <label class="label">Komentar (opsional)</label>
        <textarea class="textarea" id="rat-comment" placeholder="Ceritakan pengalaman Anda menggunakan layanan CleanWave...">${S.ratingForm.comment||''}</textarea>
      </div>

      <div style="display:flex;gap:10px;justify-content:flex-end;">
        <button class="btn secondary" onclick="closeModal()">Lewati</button>
        <button class="btn warning" onclick="doSubmitRating(${txId})" ${stars===0?'disabled':''}>⭐ Kirim Ulasan</button>
      </div>
    </div>`;
}

// ─── NEW Modal: Inventory Edit ────────────────────────────
function modalInvEdit({invId}){
  const item=S.inventory.find(i=>i.id===invId);
  if(!item) return '<div>Item tidak ditemukan.</div>';
  const isMachine = item.cat==='Mesin';
  return `
    <div>
      <div class="modal-title">${item.icon} Edit ${item.name}</div>
      <div class="modal-sub">Kategori: ${item.cat}</div>
      ${isMachine?`
        <div class="mb14">
          <label class="label">Status Mesin</label>
          <select class="input" id="inv-status">
            ${['Aktif','Maintenance','Rusak'].map(s=>`<option ${item.status===s?'selected':''}>${s}</option>`).join('')}
          </select>
        </div>
        <div class="mb14">
          <label class="label">Tanggal Maintenance Terakhir</label>
          <input class="input" id="inv-maint" type="date" value="${item.lastMaint||''}" />
        </div>`:`
        <div class="mb14">
          <label class="label">Stok Saat Ini (${item.unit})</label>
          <input class="input" id="inv-stock" type="number" min="0" step="0.5" value="${item.stock}" />
        </div>
        <div style="background:#F0F9FF;border-radius:10px;padding:12px;margin-bottom:16px;font-size:13px;">
          <div style="color:#64748B;">Stok minimum: <strong>${item.minStock} ${item.unit}</strong></div>
          <div style="color:#64748B;margin-top:4px;">Harga per ${item.unit}: <strong>${item.price?rp(item.price):'-'}</strong></div>
        </div>`}
      <div class="mb14">
        <label class="label">Catatan (opsional)</label>
        <input class="input" id="inv-note" placeholder="Keterangan tambahan..." value="${item.note||''}" />
      </div>
      <div style="display:flex;gap:10px;justify-content:flex-end;">
        <button class="btn secondary" onclick="closeModal()">Batal</button>
        <button class="btn success" onclick="doSaveInventory('${invId}')">💾 Simpan</button>
      </div>
    </div>`;
}

// ═══════════════════════════════════════════════════════════
// ACTIONS — STAFF
// ═══════════════════════════════════════════════════════════
function doInputBerat(txId, surcharge, pricePerKg){
  const kg=parseFloat(document.getElementById('m-kg')?.value);
  const det=document.getElementById('m-det')?.value;
  const mach=document.getElementById('m-mach')?.value;
  const estRaw=document.getElementById('m-est')?.value;
  if(!kg||kg<=0){ toast('Masukkan berat yang valid!','error'); return; }

  const price=Math.ceil(kg*pricePerKg)+surcharge;
  const pts=Math.floor(price/1000);
  const est=estRaw?new Date(estRaw).toISOString():calcEstimated('cuci-setrika',0);

  S.transactions=S.transactions.map(t=>{
    if(t.id!==txId) return t;
    return {...t, kg, detergent:det, machine:mach, estimatedDone:est, price, pts, status:'menunggu-bayar'};
  });

  // Kurangi stok deterjen yang dipakai
  const detItem = S.inventory.find(i=>i.cat==='Deterjen' && i.name===det);
  if(detItem){ S.inventory = S.inventory.map(i=>i.id===detItem.id?{...i,stock:Math.max(0,i.stock-Math.ceil(kg*0.05))}:i); }

  const tx=S.transactions.find(t=>t.id===txId);
  const cust=S.customers.find(c=>c.id===tx.customerId);

  addNotif(tx.customerId, txId, 'invoice-ready',
    `Invoice laundry Anda siap! Order ${tx.qNum} — ${tx.service} (${kg} kg) = ${rp(price)}. Estimasi selesai: ${fmtEst(est)}. Mohon segera lakukan pembayaran.`);

  save();
  closeModal();
  renderStaff();
  toast(`Berat tersimpan! Invoice ${rp(price)} telah dikirim ke ${cust?.name}.`,'success');

  setTimeout(()=>{
    openModal('wa-notif',{
      txId,
      custPhone: cust?.phone||'-',
      msg: `Halo ${cust?.name}! 👋\n\nInvoice laundry Anda sudah siap:\n🏷️ Order: ${tx.qNum}\n👕 Layanan: ${tx.service}\n⚖️ Berat: ${kg} kg\n🧴 Deterjen: ${det}\n💰 Total: ${rp(price)}\n⏰ Estimasi selesai: ${fmtEst(est)}\n\nSilakan lakukan pembayaran. Terima kasih! 🙏\n\n_CleanWave Laundry_`
    });
  }, 500);
}

function doKonfirmBayar(txId){
  S.transactions=S.transactions.map(t=>{
    if(t.id!==txId) return t;
    return {...t, status:'diproses', paidAt:new Date().toISOString().slice(0,10)};
  });
  const tx=S.transactions.find(t=>t.id===txId);
  const cust=S.customers.find(c=>c.id===tx.customerId);

  S.customers=S.customers.map(c=>{
    if(c.id!==tx.customerId) return c;
    const newPts=c.pts+tx.pts;
    return {...c, pts:newPts, tier:getTier(newPts).name};
  });
  if(S.loggedIn?.id===tx.customerId){
    const updated=S.customers.find(c=>c.id===tx.customerId);
    S.loggedIn={...S.loggedIn, pts:updated.pts, tier:updated.tier};
  }

  addNotif(tx.customerId, txId, 'processing',
    `Pembayaran diterima! Laundry ${tx.qNum} sedang dalam proses. Estimasi selesai: ${fmtEst(tx.estimatedDone)}.`);

  save(); closeModal(); renderStaff();
  toast(`Pembayaran dikonfirmasi! +${tx.pts} poin untuk ${cust?.name}.`,'success');

  setTimeout(()=>{
    openModal('wa-notif',{
      txId,
      custPhone:cust?.phone||'-',
      msg:`Halo ${cust?.name}! 👋\n\nPembayaran Anda sudah kami terima ✅\n\n🫧 Laundry Anda sedang dalam proses pencucian.\n⏰ Estimasi selesai: ${fmtEst(tx.estimatedDone)}\n\nKami akan kabari lagi saat sudah selesai! 😊\n\n_CleanWave Laundry_`
    });
  },500);
}

function doUpdateStatus(txId, newStatus){
  S.transactions=S.transactions.map(t=>{
    if(t.id!==txId) return t;
    return {...t, status:newStatus, notified: newStatus==='selesai'?false:t.notified};
  });
  const tx=S.transactions.find(t=>t.id===txId);
  const cust=S.customers.find(c=>c.id===tx.customerId);
  save(); closeModal(); renderStaff();

  if(newStatus==='selesai'){
    addNotif(tx.customerId, txId, 'order-done',
      `🎉 Laundry Anda ${tx.qNum} sudah selesai dan ${tx.pickupMethod==='dijemput'?'siap diantarkan ke alamat Anda':'siap diambil di outlet'}!`);
    save();
    toast(`Pesanan selesai! Notifikasi dikirim ke ${cust?.name}.`,'success');
    setTimeout(()=>{
      openModal('wa-notif',{
        txId, custPhone:cust?.phone||'-',
        msg:`Halo ${cust?.name}! 🎉\n\nLaundry Anda sudah SELESAI!\n\n🏷️ Order: ${tx.qNum}\n👕 ${tx.service} (${tx.kg} kg)\n\n${tx.pickupMethod==='dijemput'?'🛵 Kurir kami akan segera mengantarkan ke alamat Anda.':'🏪 Silakan diambil di outlet kami.'}\n\nTerima kasih sudah mempercayai CleanWave! 💙\n\n_CleanWave Laundry_`
      });
    },500);
  } else {
    toast('Status berhasil diperbarui.','success');
  }
}

// ─── NEW: Save Inventory ──────────────────────────────────
function doSaveInventory(invId){
  const item=S.inventory.find(i=>i.id===invId);
  if(!item) return;
  const isMachine=item.cat==='Mesin';
  const note=document.getElementById('inv-note')?.value||'';
  if(isMachine){
    const status=document.getElementById('inv-status')?.value||'Aktif';
    const lastMaint=document.getElementById('inv-maint')?.value||item.lastMaint;
    S.inventory=S.inventory.map(i=>i.id===invId?{...i,status,lastMaint,note}:i);
  } else {
    const stock=parseFloat(document.getElementById('inv-stock')?.value);
    if(isNaN(stock)||stock<0){ toast('Jumlah stok tidak valid!','error'); return; }
    S.inventory=S.inventory.map(i=>i.id===invId?{...i,stock,note}:i);
  }
  save(); closeModal(); renderStaff();
  toast(`${item.name} berhasil diperbarui!`,'success');
}

function staffLogout(){ S.staffAuth=null; S.mode='customer'; S.staffPage='dashboard'; save(); render(); }

// ═══════════════════════════════════════════════════════════
// ACTIONS — CUSTOMER
// ═══════════════════════════════════════════════════════════
function syncOrderForm(){
  ['name','phone','address','notes'].forEach(f=>{
    const el=document.getElementById('of-'+f);
    if(el) S.orderForm[f]=el.value;
  });
}
function selectService(id){ syncOrderForm(); S.orderForm.serviceId=id; render(); }
function selectPickup(id){ syncOrderForm(); S.orderForm.pickupMethod=id; render(); }
function selectPayment(id){ syncOrderForm(); S.orderForm.paymentMethod=id; render(); }

function submitOrder(){
  syncOrderForm();
  const {name,phone,address,serviceId,pickupMethod,paymentMethod,notes}=S.orderForm;
  if(!name||!phone){ toast('Nama dan nomor HP wajib diisi!','error'); return; }
  if(pickupMethod==='dijemput'&&!address.trim()){ toast('Masukkan alamat penjemputan!','error'); return; }

  const svc=SERVICES.find(s=>s.id===serviceId);
  let cust=S.customers.find(c=>c.phone===phone);
  if(!cust){
    cust={id:Date.now(),name,phone,email:'',joinDate:new Date().toISOString().slice(0,10),pts:0,tier:'Bronze'};
    S.customers=[...S.customers,cust];
  }

  const qNum=nextQueue();
  const tx={
    id:Date.now(), customerId:cust.id, qNum,
    date:new Date().toISOString().slice(0,10),
    kg:null, serviceId, service:svc.name, price:null,
    status:'menunggu-timbang', pts:0,
    detergent:null, machine:null,
    pickupMethod, paymentMethod, address, notes,
    estimatedDone:null, paidAt:null, notified:false,
  };
  S.transactions=[...S.transactions,tx];
  S.orderTx=tx; S.orderDone=true;
  save(); render();
  toast('Pesanan berhasil dibuat! 🎉');
}

function resetOrderForm(){
  S.orderForm={
    name:S.loggedIn?.name||'', phone:S.loggedIn?.phone||'',
    address:'', serviceId:'cuci-setrika',
    pickupMethod:'antar-mandiri', paymentMethod:'cash', notes:''
  };
  S.orderDone=false; S.orderTx=null; render();
}

function handleLogin(){
  const phone=document.getElementById('lf-phone')?.value||'';
  const cust=S.customers.find(c=>c.phone===phone);
  if(!cust){ toast('Nomor HP tidak ditemukan!','error'); return; }
  S.loggedIn=cust;
  S.orderForm.name=cust.name; S.orderForm.phone=cust.phone;
  save(); setPage('home'); toast(`Selamat datang, ${cust.name}! 👋`);
}

function handleRegister(){
  const name=document.getElementById('rf-name')?.value||'';
  const phone=document.getElementById('rf-phone')?.value||'';
  const email=document.getElementById('rf-email')?.value||'';
  if(!name||!phone){ toast('Nama dan HP wajib diisi!','error'); return; }
  if(S.customers.find(c=>c.phone===phone)){ toast('Nomor HP sudah terdaftar!','error'); return; }
  const c={id:Date.now(),name,phone,email,joinDate:new Date().toISOString().slice(0,10),pts:0,tier:'Bronze'};
  S.customers=[...S.customers,c];
  S.loggedIn=c;
  S.orderForm.name=c.name; S.orderForm.phone=c.phone;
  save(); setPage('home'); toast(`Selamat bergabung, ${name}! 🎉`);
}

function handleStaffLogin(){
  const u=document.getElementById('sl-user')?.value||'';
  const p=document.getElementById('sl-pass')?.value||'';
  const acc=STAFF_ACCOUNTS.find(a=>a.username===u&&a.password===p);
  if(!acc){ toast('Username atau password salah!','error'); return; }
  S.staffAuth=acc; S.mode='staff'; S.staffPage='dashboard';
  save(); render(); toast(`Selamat datang, ${acc.name}!`);
}

function logout(){ S.loggedIn=null; save(); setPage('home'); toast('Berhasil keluar.','info'); }

function checkStatus(){
  const q=S.checkStatusQuery.trim();
  if(!q){ toast('Masukkan nomor order atau HP!','error'); return; }
  const tx=S.transactions.find(t=>t.qNum===q.toUpperCase()||
    (S.customers.find(c=>c.phone===q)?.id===t.customerId));
  S.checkStatusResult=tx||null;
  render();
}

function redeemReward(id){
  if(!S.loggedIn){ toast('Login dulu!','error'); return; }
  const r=REWARDS.find(x=>x.id===id);
  if(S.loggedIn.pts<r.pts){ toast('Poin tidak cukup!','error'); return; }
  S.loggedIn.pts-=r.pts; S.loggedIn.tier=getTier(S.loggedIn.pts).name;
  S.customers=S.customers.map(c=>c.id===S.loggedIn.id?S.loggedIn:c);
  save(); render(); toast(`🎉 Berhasil tukar: ${r.name}!`);
}

// ─── NEW: Rating Actions ──────────────────────────────────
function selectStar(n, txId){
  S.ratingForm.stars=n;
  openModal('rating', {txId});
}

function doSubmitRating(txId){
  const stars=S.ratingForm.stars;
  const comment=document.getElementById('rat-comment')?.value||'';
  if(stars===0){ toast('Pilih bintang terlebih dahulu!','error'); return; }
  const tx=S.transactions.find(t=>t.id===txId);
  if(!tx){ toast('Pesanan tidak ditemukan.','error'); return; }
  S.ratings.push({
    id:'r'+Date.now(),
    customerId:tx.customerId,
    txId,
    stars,
    comment:comment.trim(),
    createdAt:new Date().toISOString(),
  });
  S.ratingForm={stars:0,comment:''};
  save(); closeModal();
  toast(`Terima kasih atas ulasan Anda! ⭐`,'success');
  render();
}

// ═══════════════════════════════════════════════════════════
// NAVIGATION
// ═══════════════════════════════════════════════════════════
function setPage(id){ S.page=id; render(); window.scrollTo(0,0); }
function setStaffPage(id){ S.staffPage=id; renderStaff(); }

// ═══════════════════════════════════════════════════════════
// ██████████ CUSTOMER RENDER ██████████
// ═══════════════════════════════════════════════════════════
function renderCustomerApp(){
  const uc=S.loggedIn?unreadCount(S.loggedIn.id):0;
  const navItems=[
    {id:'home',label:'Beranda',icon:'🏠'},
    {id:'order',label:'Pesan',icon:'📦'},
    {id:'cek-status',label:'Cek Status',icon:'🔍'},
    {id:'membership',label:'Member',icon:'⭐'},
  ];
  if(S.loggedIn){
    navItems.push({id:'profile',label:S.loggedIn.name.split(' ')[0],icon:'👤'});
  } else {
    navItems.push({id:'login',label:'Masuk',icon:'👤'});
  }

  const pages={
    home:renderHome, order:renderOrder, 'cek-status':renderCekStatus,
    membership:renderMembership, profile:renderProfile, login:renderLogin,
  };
  const pageHtml=(pages[S.page]||renderHome)();

  return `
    <div class="c-app">
      <header class="c-header">
        <div class="c-logo" onclick="setPage('home')">🌊 CleanWave</div>
        <nav class="c-nav">
          ${navItems.map(n=>`
            <button class="c-nav-btn ${S.page===n.id?'active':''}" onclick="setPage('${n.id}')">
              <span>${n.icon}</span>${n.label}
            </button>`).join('')}
          ${S.loggedIn?`
            <button class="c-nav-btn" onclick="openModal('notif-list',{custId:${S.loggedIn.id}})">
              <div class="bell-wrap">🔔${uc>0?`<span class="bell-badge">${uc}</span>`:''}</div>
            </button>`:''}
          <button class="c-nav-btn" style="font-size:11px;opacity:.7;" onclick="setPage('staff-login')">
            🔑 Karyawan
          </button>
        </nav>
      </header>
      <main class="c-content">${pageHtml}</main>
    </div>`;
}

// ─── Home ────────────────────────────────────────────────
function renderHome(){
  const avg=avgRating();
  const recentReviews=S.ratings.filter(r=>r.comment).sort((a,b)=>b.id.localeCompare(a.id)).slice(0,3);
  return `
    <div class="hero">
      <div style="position:absolute;right:40px;top:50%;transform:translateY(-50%);font-size:120px;opacity:.15;">👕</div>
      <div style="font-size:12px;font-weight:700;background:rgba(255,255,255,.2);display:inline-block;padding:4px 14px;border-radius:99px;margin-bottom:16px;letter-spacing:1px;">
        UMKM LAUNDRY · INDUSTRY 4.0 READY
      </div>
      <h1>CleanWave<br/>Laundry 🌊</h1>
      <p style="font-size:15px;opacity:.9;max-width:400px;margin:0 0 28px;">
        Layanan laundry profesional dengan sistem digital terintegrasi. Titip baju, kami urus semuanya.
      </p>
      <div style="display:flex;gap:12px;flex-wrap:wrap;">
        <button class="btn lg" onclick="setPage('order')">📦 Pesan Sekarang</button>
        <button class="btn" style="background:rgba(255,255,255,.2);" onclick="setPage('cek-status')">🔍 Cek Status Pesanan</button>
      </div>
      ${avg>0?`
        <div style="margin-top:20px;display:inline-flex;align-items:center;gap:8px;background:rgba(255,255,255,.2);padding:6px 16px;border-radius:99px;">
          <span style="font-size:16px;">${renderStars(Math.round(avg),16)}</span>
          <span style="font-weight:800;font-size:15px;">${avg}</span>
          <span style="font-size:13px;opacity:.9;">(${S.ratings.length} ulasan)</span>
        </div>`:''}
    </div>

    <div class="grid4" style="margin-bottom:20px;">
      ${[
        {icon:'👥',val:S.customers.length,label:'Pelanggan Aktif',bg:'#EFF6FF',ic:'#3B82F6'},
        {icon:'📦',val:S.transactions.length,label:'Total Transaksi',bg:'#F0FDF4',ic:'#10B981'},
        {icon:'⭐',val:S.customers.filter(c=>c.tier==='Gold').length,label:'Member Gold',bg:'#FFFBEB',ic:'#F59E0B'},
        {icon:'🫧',val:S.transactions.filter(t=>t.status==='diproses').length,label:'Sedang Diproses',bg:'#F5F3FF',ic:'#8B5CF6'},
      ].map(s=>`
        <div class="card" style="text-align:center;padding:18px;background:${s.bg};box-shadow:none;border:1.5px solid ${s.ic}22;">
          <div style="font-size:30px;margin-bottom:6px;">${s.icon}</div>
          <div style="font-size:28px;font-weight:900;color:${s.ic};">${s.val}</div>
          <div style="font-size:12px;color:#64748B;font-weight:600;">${s.label}</div>
        </div>`).join('')}
    </div>

    <div class="card">
      <div class="title">Layanan Kami</div>
      <div class="subtitle">Pilih layanan sesuai kebutuhan. Harga dihitung setelah penimbangan.</div>
      <div class="grid2">
        ${SERVICES.map(s=>`
          <div onclick="setPage('order')" style="background:#F8FAFC;border-radius:12px;padding:16px;border:1.5px solid #E2E8F0;cursor:pointer;transition:all .2s;" onmouseover="this.style.borderColor='#0EA5E9';this.style.background='#F0F9FF'" onmouseout="this.style.borderColor='#E2E8F0';this.style.background='#F8FAFC'">
            <div style="font-size:28px;margin-bottom:8px;">${s.icon}</div>
            <div style="font-weight:800;font-size:15px;color:#0369A1;margin-bottom:4px;">${s.name}</div>
            <div style="font-size:12px;color:#64748B;margin-bottom:10px;">${s.desc}</div>
            <div style="font-size:18px;font-weight:900;color:#0EA5E9;">
              Rp ${s.price.toLocaleString('id')}<span style="font-size:12px;font-weight:500;color:#94A3B8;">/kg</span>
            </div>
            <div style="font-size:11px;color:#94A3B8;margin-top:4px;">⏱️ Estimasi ${s.hours} jam</div>
          </div>`).join('')}
      </div>
    </div>

    <div class="card" style="background:linear-gradient(135deg,#FEF3C7,#FDE68A);border:1.5px solid #FCD34D;">
      <div style="display:flex;align-items:center;gap:16px;">
        <div style="font-size:48px;">⭐</div>
        <div style="flex:1;">
          <div style="font-weight:800;font-size:18px;color:#92400E;margin-bottom:4px;">Program Membership CleanWave</div>
          <div style="font-size:13px;color:#78350F;">Kumpulkan poin dari setiap transaksi & tukarkan dengan hadiah menarik!</div>
        </div>
        <button class="btn warning" style="white-space:nowrap;" onclick="setPage('membership')">Lihat Hadiah</button>
      </div>
    </div>

    ${recentReviews.length>0?`
    <div class="card">
      <div class="title">💬 Ulasan Pelanggan</div>
      <div class="subtitle">Apa kata mereka yang sudah menggunakan CleanWave?</div>
      <div style="display:flex;align-items:center;gap:16px;background:#FFFBEB;border-radius:12px;padding:16px;margin-bottom:20px;">
        <div style="text-align:center;">
          <div style="font-size:40px;font-weight:900;color:#D97706;line-height:1;">${avg}</div>
          <div style="font-size:18px;margin:4px 0;">${renderStars(Math.round(avg),18)}</div>
          <div style="font-size:12px;color:#92400E;font-weight:600;">${S.ratings.length} ulasan</div>
        </div>
        <div style="flex:1;margin-left:8px;">
          ${[5,4,3,2,1].map(s=>{
            const cnt=S.ratings.filter(r=>r.stars===s).length;
            const pct=S.ratings.length?Math.round(cnt/S.ratings.length*100):0;
            return `<div style="display:flex;align-items:center;gap:8px;margin-bottom:5px;font-size:12px;">
              <span style="color:#D97706;font-weight:700;width:10px;">${s}</span>
              <span style="color:#D97706;font-size:12px;">★</span>
              <div style="flex:1;background:#F1F5F9;border-radius:99px;height:6px;overflow:hidden;">
                <div style="background:#F59E0B;height:6px;width:${pct}%;border-radius:99px;"></div>
              </div>
              <span style="color:#64748B;width:24px;">${cnt}</span>
            </div>`;}).join('')}
        </div>
      </div>
      ${recentReviews.map(r=>{
        const cust=S.customers.find(c=>c.id===r.customerId);
        const tx=S.transactions.find(t=>t.id===r.txId);
        return `
          <div class="review-card">
            <div class="review-header">
              <div>
                <div class="review-name">${maskName(cust?.name||'Pelanggan')}</div>
                <div style="font-size:13px;margin-top:2px;">${renderStars(r.stars,14)} <span style="color:#64748B;font-size:12px;">${tx?.service||''}</span></div>
              </div>
              <div class="review-date">${fmtEst(r.createdAt)}</div>
            </div>
            ${r.comment?`<div class="review-comment">"${r.comment}"</div>`:''}
          </div>`;}).join('')}
    </div>`:''}`;
}

// ─── Order ────────────────────────────────────────────────
function renderOrder(){
  if(S.orderDone && S.orderTx){
    const tx=S.orderTx;
    return `
      <div class="card">
        <div style="text-align:center;padding:20px 0;">
          <div style="font-size:72px;margin-bottom:16px;">🎉</div>
          <div style="font-size:24px;font-weight:900;color:#0369A1;margin-bottom:8px;">Pesanan Berhasil Dibuat!</div>
          <div class="queue-pill" style="background:#0EA5E9;color:#fff;display:inline-flex;margin-bottom:20px;">
            📋 Nomor Antrian: <strong>${tx.qNum}</strong>
          </div>
          <div style="background:#F0F9FF;border-radius:14px;padding:20px;max-width:400px;margin:0 auto 20px;text-align:left;">
            ${[
              ['Layanan', tx.service],
              ['Pengambilan', pickLbl(tx.pickupMethod)],
              ['Pembayaran', payLbl(tx.paymentMethod)],
              tx.address?['Alamat',tx.address]:null,
            ].filter(Boolean).map(([k,v])=>`
              <div style="display:flex;justify-content:space-between;margin-bottom:8px;font-size:14px;">
                <span style="color:#64748B;">${k}</span><strong style="text-align:right;max-width:55%;">${v}</strong>
              </div>`).join('')}
            <hr class="divider">
            ${statusBadge('menunggu-timbang')}
          </div>
          <div style="background:#FEF3C7;border-radius:12px;padding:14px;max-width:400px;margin:0 auto 24px;font-size:13px;color:#92400E;font-weight:600;">
            ⚖️ Berat akan ditimbang oleh karyawan. Invoice & estimasi waktu selesai akan dikirim via WhatsApp setelah penimbangan.
          </div>
          <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">
            <button class="btn" onclick="resetOrderForm()">Pesan Lagi</button>
            <button class="btn secondary" onclick="setPage('cek-status')">🔍 Cek Status</button>
          </div>
        </div>
      </div>`;
  }

  const svc=SERVICES.find(s=>s.id===S.orderForm.serviceId)||SERVICES[0];

  return `
    <div>
      <div class="title">📦 Pesan Laundry</div>
      <div class="subtitle">Isi form, antar ke outlet atau tunggu kurir kami. Berat ditimbang oleh karyawan.</div>
      <div style="display:grid;grid-template-columns:1.4fr 1fr;gap:20px;" class="order-cols">

        <div>
          <div class="card">
            <div style="font-weight:700;font-size:16px;margin-bottom:16px;color:#0369A1;">👤 Data Pelanggan</div>
            <div class="mb14">
              <label class="label">Nama Lengkap</label>
              <input class="input" id="of-name" value="${S.orderForm.name}" placeholder="Masukkan nama lengkap" />
            </div>
            <div class="mb14">
              <label class="label">Nomor HP</label>
              <input class="input" id="of-phone" value="${S.orderForm.phone}" placeholder="08xxxxxxxxxx" />
            </div>
          </div>

          <div class="card">
            <div style="font-weight:700;font-size:16px;margin-bottom:4px;color:#0369A1;">🚀 Metode Pengambilan</div>
            <div class="subtitle">Pilih cara penyerahan pakaian</div>
            <div style="display:flex;flex-direction:column;gap:10px;">
              ${PICKUP_OPTS.map(p=>`
                <div class="opt-card ${S.orderForm.pickupMethod===p.id?'selected':''}" onclick="selectPickup('${p.id}')">
                  <div style="font-size:28px;">${p.icon}</div>
                  <div style="flex:1;"><div style="font-weight:700;font-size:14px;">${p.title}</div><div style="font-size:12px;color:#64748B;">${p.desc}</div></div>
                  <div class="opt-dot"></div>
                </div>`).join('')}
            </div>
            ${S.orderForm.pickupMethod==='dijemput'?`
              <div style="margin-top:14px;">
                <label class="label">📍 Alamat Penjemputan</label>
                <textarea class="textarea" id="of-address" placeholder="Nama jalan, no. rumah, RT/RW, kelurahan...">${S.orderForm.address}</textarea>
              </div>`:'<div id="of-address-hidden"></div>'}
          </div>

          <div class="card">
            <div style="font-weight:700;font-size:16px;margin-bottom:16px;color:#0369A1;">🧺 Pilih Layanan</div>
            ${SERVICES.map(s=>`
              <div onclick="selectService('${s.id}')" style="border:2px solid ${S.orderForm.serviceId===s.id?'#0EA5E9':'#E2E8F0'};border-radius:12px;padding:14px;margin-bottom:10px;cursor:pointer;background:${S.orderForm.serviceId===s.id?'#F0F9FF':'#fff'};transition:all .2s;">
                <div style="display:flex;justify-content:space-between;align-items:center;">
                  <div style="display:flex;align-items:center;gap:10px;">
                    <span style="font-size:24px;">${s.icon}</span>
                    <div>
                      <div style="font-weight:700;color:${S.orderForm.serviceId===s.id?'#0369A1':'#0F172A'};">${s.name}</div>
                      <div style="font-size:12px;color:#94A3B8;">${s.desc} · ⏱️ ${s.hours} jam</div>
                    </div>
                  </div>
                  <div style="font-weight:800;color:#0EA5E9;white-space:nowrap;">${rp(s.price)}/kg</div>
                </div>
              </div>`).join('')}
            <div class="weight-box" style="margin-top:4px;">
              <div style="font-size:28px;">⚖️</div>
              <div>
                <div style="font-size:12px;font-weight:800;color:#92400E;text-transform:uppercase;letter-spacing:.5px;">Berat Laundry</div>
                <div style="font-size:13px;color:#78350F;margin-top:2px;">Ditimbang & dicatat oleh karyawan setelah laundry diterima</div>
              </div>
            </div>
          </div>

          <div class="card">
            <div style="font-weight:700;font-size:16px;margin-bottom:4px;color:#0369A1;">💳 Metode Pembayaran</div>
            <div class="subtitle">Pembayaran dilakukan setelah berat ditimbang</div>
            <div style="display:flex;flex-direction:column;gap:10px;">
              ${PAYMENT_OPTS.map(p=>`
                <div class="opt-card ${S.orderForm.paymentMethod===p.id?'selected':''}" onclick="selectPayment('${p.id}')">
                  <div style="font-size:28px;">${p.icon}</div>
                  <div style="flex:1;"><div style="font-weight:700;font-size:14px;">${p.title}</div><div style="font-size:12px;color:#64748B;">${p.desc}</div></div>
                  <div class="opt-dot"></div>
                </div>`).join('')}
            </div>
          </div>

          <div class="card">
            <div style="font-weight:700;font-size:16px;margin-bottom:12px;color:#0369A1;">📝 Catatan (Opsional)</div>
            <textarea class="textarea" id="of-notes" placeholder="Alergi deterjen, instruksi khusus, dll.">${S.orderForm.notes}</textarea>
          </div>
        </div>

        <div>
          <div class="card" style="position:sticky;top:76px;">
            <div style="font-weight:700;font-size:16px;margin-bottom:16px;color:#0369A1;">🧾 Ringkasan Pesanan</div>
            ${[
              ['Layanan', svc.name],
              ['Tarif', rp(svc.price)+'/kg'],
              ['Est. Waktu', svc.hours+' jam'],
              ['Pengambilan', pickLbl(S.orderForm.pickupMethod)],
              ['Pembayaran', payLbl(S.orderForm.paymentMethod)],
            ].map(([k,v])=>`
              <div style="display:flex;justify-content:space-between;margin-bottom:10px;font-size:14px;">
                <span style="color:#64748B;">${k}</span><span style="font-weight:600;">${v}</span>
              </div>`).join('')}
            ${S.orderForm.pickupMethod==='dijemput'?`
              <div style="display:flex;justify-content:space-between;margin-bottom:10px;font-size:14px;">
                <span style="color:#64748B;">Biaya Jemput</span><span style="font-weight:600;color:#EF4444;">+Rp 5.000</span>
              </div>`:''}
            <hr class="divider">
            <div style="background:#F8FAFC;border-radius:10px;padding:12px;margin-bottom:14px;border:1.5px dashed #CBD5E1;">
              <div style="font-size:12px;color:#64748B;font-weight:600;">⚖️ Total Harga</div>
              <div style="font-size:14px;font-weight:800;color:#94A3B8;margin-top:4px;">Dihitung setelah penimbangan</div>
            </div>
            <div style="background:#EFF6FF;border-radius:10px;padding:10px 14px;margin-bottom:18px;font-size:13px;color:#1E40AF;font-weight:600;">
              ⭐ Poin = Total Harga ÷ Rp 1.000<br/>
              🔔 Invoice dikirim via WhatsApp setelah timbang
            </div>
            <button class="btn block lg" onclick="submitOrder()">✅ Konfirmasi Pesanan</button>
            <div style="font-size:11px;color:#94A3B8;text-align:center;margin-top:10px;">Berat ditimbang saat laundry diterima karyawan</div>
          </div>
        </div>
      </div>
    </div>`;
}

// ─── Cek Status ───────────────────────────────────────────
function renderCekStatus(){
  const myOrders = S.loggedIn
    ? S.transactions.filter(t=>t.customerId===S.loggedIn.id&&t.status!=='selesai-bayar').sort((a,b)=>b.id-a.id)
    : [];

  return `
    <div>
      <div class="title">🔍 Cek Status Pesanan</div>
      <div class="subtitle">Cek status tanpa login dengan nomor order atau nomor HP</div>

      <div class="card">
        <div style="display:flex;gap:12px;align-items:flex-end;">
          <div style="flex:1;">
            <label class="label">Nomor Order (CW-xxx) atau Nomor HP</label>
            <input class="input" id="cs-query" value="${S.checkStatusQuery}" placeholder="Contoh: CW-001 atau 08xxxxxxxxxx"
              onkeydown="if(event.key==='Enter'){S.checkStatusQuery=this.value;checkStatus();}" />
          </div>
          <button class="btn" onclick="S.checkStatusQuery=document.getElementById('cs-query').value;checkStatus()">Cek Status</button>
        </div>
      </div>

      ${S.checkStatusResult!==null?(()=>{
        const tx=S.checkStatusResult;
        if(!tx) return `<div class="card" style="text-align:center;color:#94A3B8;padding:32px;"><div style="font-size:48px;margin-bottom:12px;">🤷</div><div>Pesanan tidak ditemukan.</div></div>`;
        const cust=S.customers.find(c=>c.id===tx.customerId);
        return `
          <div class="card">
            <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px;flex-wrap:wrap;gap:8px;">
              <div>
                <div style="font-size:20px;font-weight:900;color:#0369A1;">${tx.qNum}</div>
                <div style="font-size:14px;color:#64748B;">${cust?.name} · ${tx.date}</div>
              </div>
              ${statusBadge(tx.status)}
            </div>
            <div class="grid2" style="margin-bottom:16px;">
              ${[
                ['Layanan', tx.service],
                ['Berat', tx.kg?tx.kg+' kg':'Menunggu timbang'],
                ['Total', tx.price!==null?rp(tx.price):'Menunggu timbang'],
                ['Pengambilan', pickLbl(tx.pickupMethod)],
                ['Estimasi Selesai', fmtEst(tx.estimatedDone)],
                ['Pembayaran', payLbl(tx.paymentMethod)],
              ].map(([k,v])=>`
                <div style="background:#F8FAFC;border-radius:10px;padding:12px;">
                  <div style="font-size:11px;color:#94A3B8;font-weight:700;text-transform:uppercase;">${k}</div>
                  <div style="font-size:14px;font-weight:700;margin-top:4px;">${v}</div>
                </div>`).join('')}
            </div>
            ${tx.status==='menunggu-bayar'?`
              <div style="background:#EDE9FE;border-radius:12px;padding:14px;margin-bottom:12px;">
                <div style="font-weight:700;color:#5B21B6;margin-bottom:4px;">💳 Invoice Siap — Menunggu Pembayaran</div>
                <div style="font-size:24px;font-weight:900;color:#6D28D9;">${rp(tx.price)}</div>
                <div style="font-size:13px;color:#7C3AED;margin-top:4px;">Silakan bayar di outlet atau tunjukkan halaman ini kepada karyawan.</div>
              </div>`:''}
            <button class="btn outline sm" onclick="openModal('invoice',{txId:${tx.id}})">🧾 Lihat Invoice Lengkap</button>
          </div>`;
      })():''}

      ${myOrders.length>0?`
        <div class="card">
          <div style="font-weight:700;font-size:16px;margin-bottom:16px;color:#0369A1;">📋 Pesanan Aktif Saya</div>
          ${myOrders.map(tx=>`
            <div style="border:1.5px solid #E2E8F0;border-radius:12px;padding:16px;margin-bottom:12px;">
              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;flex-wrap:wrap;gap:6px;">
                <div>
                  <span style="font-size:16px;font-weight:900;color:#0369A1;">${tx.qNum}</span>
                  <span style="font-size:13px;color:#64748B;margin-left:10px;">${tx.service}</span>
                </div>
                ${statusBadge(tx.status)}
              </div>
              ${tx.estimatedDone?`
                <div style="background:#F0F9FF;border-radius:8px;padding:8px 12px;margin-bottom:10px;font-size:13px;">
                  ⏰ Estimasi selesai: <strong>${fmtEst(tx.estimatedDone)}</strong>
                </div>`:''}
              ${tx.status==='menunggu-bayar'?`
                <div style="background:#EDE9FE;border-radius:8px;padding:10px 14px;margin-bottom:10px;display:flex;justify-content:space-between;align-items:center;">
                  <span style="font-size:13px;color:#5B21B6;font-weight:600;">💳 Total: ${rp(tx.price)}</span>
                  <button class="btn purple sm" onclick="openModal('invoice',{txId:${tx.id}})">Lihat Invoice</button>
                </div>`:''}
              <button class="btn outline sm" onclick="openModal('invoice',{txId:${tx.id}})">🧾 Detail</button>
            </div>`).join('')}
        </div>`:''}
    </div>`;
}

// ─── Membership ───────────────────────────────────────────
function renderMembership(){
  const tier=S.loggedIn?getTier(S.loggedIn.pts):null;
  return `
    <div>
      <div class="title">⭐ Program Membership</div>
      <div class="subtitle">Kumpulkan poin dari setiap transaksi dan nikmati hadiahnya</div>

      ${S.loggedIn?`
        <div style="background:linear-gradient(135deg,${tier.color},${tier.color}bb);border-radius:20px;padding:28px 32px;color:#fff;margin-bottom:24px;position:relative;overflow:hidden;">
          <div style="position:absolute;right:24px;top:50%;transform:translateY(-50%);font-size:80px;opacity:.15;">💳</div>
          <div style="font-size:11px;font-weight:700;opacity:.8;letter-spacing:2px;margin-bottom:10px;">CLEANWAVE MEMBER CARD</div>
          <div style="font-size:26px;font-weight:900;margin-bottom:3px;">${S.loggedIn.name}</div>
          <div style="font-size:13px;opacity:.8;margin-bottom:18px;">${S.loggedIn.phone}</div>
          <div style="display:flex;align-items:baseline;gap:8px;">
            <span style="font-size:44px;font-weight:900;">${S.loggedIn.pts}</span>
            <span style="opacity:.8;">Poin</span>
            <span style="margin-left:auto;background:rgba(255,255,255,.3);padding:4px 14px;border-radius:99px;font-weight:800;font-size:14px;">${tier.name} ★</span>
          </div>
          <div style="margin-top:8px;font-size:12px;opacity:.7;">
            ${tier.name==='Bronze'?`${200-S.loggedIn.pts} poin lagi ke Silver`:tier.name==='Silver'?`${500-S.loggedIn.pts} poin lagi ke Gold`:'Tier tertinggi! 🏆'}
          </div>
        </div>`:`
        <div class="card" style="background:#FEF3C7;border:1.5px solid #FCD34D;text-align:center;padding:28px;">
          <div style="font-size:48px;margin-bottom:12px;">🔒</div>
          <div style="font-weight:700;font-size:16px;color:#92400E;margin-bottom:8px;">Login untuk lihat poin Anda</div>
          <button class="btn warning" onclick="setPage('login')">Login Sekarang</button>
        </div>`}

      <div class="card">
        <div style="font-weight:700;font-size:16px;margin-bottom:16px;color:#0369A1;">Level Keanggotaan</div>
        <div class="grid3">
          ${[
            {name:'Bronze',range:'0–199 poin',perks:'1 poin per Rp 1.000',color:'#92400E',bg:'#FEF9C3'},
            {name:'Silver',range:'200–499 poin',perks:'1 poin + prioritas antrian',color:'#6B7280',bg:'#F3F4F6'},
            {name:'Gold',range:'500+ poin',perks:'1 poin + prioritas + diskon 5%',color:'#D97706',bg:'#FEF3C7'},
          ].map(t=>`
            <div style="background:${t.bg};border-radius:12px;padding:16px;border:2px solid ${S.loggedIn?.tier===t.name?t.color:'transparent'};">
              <div style="font-weight:800;color:${t.color};font-size:17px;margin-bottom:4px;">${t.name} ★</div>
              <div style="font-size:12px;color:#64748B;margin-bottom:6px;">${t.range}</div>
              <div style="font-size:12px;font-weight:600;color:#374151;">${t.perks}</div>
            </div>`).join('')}
        </div>
      </div>

      <div class="card">
        <div style="font-weight:700;font-size:16px;margin-bottom:4px;color:#0369A1;">Tukar Poin</div>
        <div class="subtitle">Poin didapat setelah pembayaran dikonfirmasi</div>
        <div class="grid2">
          ${REWARDS.map(r=>{
            const can=S.loggedIn&&S.loggedIn.pts>=r.pts;
            return `
              <div style="border:2px solid ${can?'#FCD34D':'#E2E8F0'};border-radius:14px;padding:16px;background:${can?'#FFFBEB':'#FAFAFA'};">
                <div style="font-size:32px;margin-bottom:8px;">${r.icon}</div>
                <div style="font-weight:800;font-size:14px;margin-bottom:4px;">${r.name}</div>
                <div style="font-size:12px;color:#64748B;margin-bottom:12px;">${r.desc}</div>
                <div style="display:flex;align-items:center;justify-content:space-between;">
                  <span style="font-weight:900;color:#D97706;">${r.pts} ⭐</span>
                  <button class="btn sm ${can?'warning':'secondary'}" ${can?`onclick="redeemReward(${r.id})"`:' disabled'}>${can?'Tukar':'Kurang'}</button>
                </div>
              </div>`;}).join('')}
        </div>
      </div>

      <div class="card">
        <div style="font-weight:700;font-size:16px;margin-bottom:16px;color:#0369A1;">Daftar Member</div>
        <table class="table">
          <thead><tr>${['Nama','No. HP','Bergabung','Tier','Poin'].map(h=>`<th class="th">${h}</th>`).join('')}</tr></thead>
          <tbody>
            ${[...S.customers].sort((a,b)=>b.pts-a.pts).map(c=>{
              const t=getTier(c.pts);
              return `<tr>
                <td class="td" style="font-weight:700;">${c.name}</td>
                <td class="td">${c.phone}</td>
                <td class="td" style="font-size:12px;color:#64748B;">${c.joinDate}</td>
                <td class="td"><span class="badge" style="background:${t.bg};color:${t.color};">${t.name} ★</span></td>
                <td class="td" style="font-weight:800;color:#D97706;">${c.pts} ⭐</td>
              </tr>`;}).join('')}
          </tbody>
        </table>
      </div>
    </div>`;
}

// ─── Profile ──────────────────────────────────────────────
function renderProfile(){
  if(!S.loggedIn) return `<div class="card" style="text-align:center;padding:40px;"><div style="font-size:48px;margin-bottom:12px;">🔒</div><button class="btn" onclick="setPage('login')">Login Dulu</button></div>`;
  const myTx=S.transactions.filter(t=>t.customerId===S.loggedIn.id).sort((a,b)=>b.id-a.id);
  const tier=getTier(S.loggedIn.pts);
  const uc=unreadCount(S.loggedIn.id);

  const hasRated=(txId)=>S.ratings.some(r=>r.txId===txId);
  const getRating=(txId)=>S.ratings.find(r=>r.txId===txId);

  return `
    <div>
      <div class="title">👤 Profil Saya</div>
      <div style="display:grid;grid-template-columns:1fr 1.6fr;gap:20px;">
        <div>
          <div class="card" style="text-align:center;">
            <div style="font-size:60px;margin-bottom:12px;">🙂</div>
            <div style="font-weight:900;font-size:20px;">${S.loggedIn.name}</div>
            <div style="font-size:13px;color:#64748B;margin-bottom:12px;">${S.loggedIn.phone}</div>
            <div class="badge mb16" style="background:${tier.bg};color:${tier.color};font-size:13px;">${tier.name} Member ★</div>
            <div style="background:#FFFBEB;border-radius:12px;padding:16px;margin-bottom:16px;">
              <div style="font-size:36px;font-weight:900;color:#D97706;">${S.loggedIn.pts}</div>
              <div style="font-size:13px;color:#92400E;font-weight:600;">Poin Saya ⭐</div>
            </div>
            ${uc>0?`
              <button class="btn outline block mb12" onclick="openModal('notif-list',{custId:${S.loggedIn.id}})">
                🔔 ${uc} Notifikasi Baru
              </button>`:''}
            <button class="btn danger block" onclick="logout()">Keluar</button>
          </div>
        </div>
        <div>
          <div class="card">
            <div style="font-weight:700;font-size:16px;margin-bottom:16px;color:#0369A1;">Riwayat Transaksi</div>
            ${myTx.length===0?`<div style="text-align:center;color:#94A3B8;padding:32px;">Belum ada transaksi</div>`:
              myTx.map(tx=>{
                const rated=hasRated(tx.id);
                const myRating=getRating(tx.id);
                return `
                <div style="border:1.5px solid #E2E8F0;border-radius:12px;padding:14px;margin-bottom:12px;">
                  <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px;flex-wrap:wrap;gap:6px;">
                    <span style="font-weight:800;color:#0369A1;">${tx.qNum}</span>
                    ${statusBadge(tx.status)}
                  </div>
                  <div style="display:flex;gap:12px;font-size:13px;color:#64748B;flex-wrap:wrap;margin-bottom:8px;">
                    <span>📅 ${tx.date}</span>
                    <span>👕 ${tx.service}</span>
                    ${tx.kg?`<span>⚖️ ${tx.kg} kg</span>`:''}
                    ${tx.price!==null?`<span style="font-weight:700;color:#0369A1;">${rp(tx.price)}</span>`:''}
                    ${tx.pts?`<span style="color:#D97706;font-weight:600;">+${tx.pts}⭐</span>`:''}
                  </div>
                  ${tx.estimatedDone?`<div style="font-size:12px;color:#64748B;">⏰ Est. selesai: <strong>${fmtEst(tx.estimatedDone)}</strong></div>`:''}

                  ${tx.status==='selesai-bayar'?`
                    <div style="margin-top:10px;padding-top:10px;border-top:1px dashed #E2E8F0;">
                      ${rated?`
                        <div style="display:flex;align-items:center;gap:6px;font-size:13px;color:#64748B;">
                          <span>Ulasan Anda:</span>
                          <span>${renderStars(myRating.stars,14)}</span>
                          ${myRating.comment?`<span style="font-style:italic;">"${myRating.comment.slice(0,40)}${myRating.comment.length>40?'...':''}"</span>`:''}
                        </div>`:`
                        <button class="btn warning sm" onclick="S.ratingForm={stars:0,comment:''};openModal('rating',{txId:${tx.id}})">
                          ⭐ Beri Nilai Layanan
                        </button>`}
                    </div>`:''}

                  <div style="display:flex;gap:6px;margin-top:8px;flex-wrap:wrap;">
                    <span class="badge" style="background:${tx.pickupMethod==='dijemput'?'#DBEAFE':'#F1F5F9'};color:${tx.pickupMethod==='dijemput'?'#1E40AF':'#374151'};font-size:11px;">${pickLbl(tx.pickupMethod)}</span>
                    <span class="badge" style="background:#F0FDF4;color:#166534;font-size:11px;">${payLbl(tx.paymentMethod)}</span>
                    <button class="btn outline sm" style="font-size:11px;padding:3px 10px;" onclick="openModal('invoice',{txId:${tx.id}})">🧾 Invoice</button>
                  </div>
                </div>`}).join('')}
          </div>
        </div>
      </div>
    </div>`;
}

// ─── Login ────────────────────────────────────────────────
function renderLogin(){
  if(S.page==='staff-login') return renderStaffLogin();
  return `
    <div style="max-width:420px;margin:0 auto;">
      <div class="card">
        <div style="text-align:center;margin-bottom:24px;">
          <div style="font-size:56px;margin-bottom:8px;">👤</div>
          <div style="font-weight:900;font-size:22px;color:#0369A1;">CleanWave Member</div>
          <div style="font-size:14px;color:#64748B;">Masuk atau daftar untuk nikmati poin reward</div>
        </div>
        <div style="display:flex;background:#F1F5F9;border-radius:12px;padding:4px;margin-bottom:24px;">
          ${['login','register'].map(tab=>`
            <button onclick="S.loginTab='${tab}';render()" style="flex:1;padding:8px 0;border:none;border-radius:10px;cursor:pointer;font-family:inherit;font-weight:700;font-size:14px;
              background:${S.loginTab===tab?'#fff':'transparent'};color:${S.loginTab===tab?'#0369A1':'#64748B'};
              box-shadow:${S.loginTab===tab?'0 2px 8px rgba(0,0,0,.08)':'none'}">
              ${tab==='login'?'Masuk':'Daftar'}
            </button>`).join('')}
        </div>
        ${S.loginTab==='login'?`
          <div class="mb14">
            <label class="label">Nomor HP</label>
            <input class="input" id="lf-phone" value="${S.loginForm.phone}" placeholder="08xxxxxxxxxx" onkeydown="if(event.key==='Enter') handleLogin()" />
          </div>
          <button class="btn block lg" onclick="handleLogin()">Masuk</button>
          <div style="font-size:12px;color:#94A3B8;text-align:center;margin-top:12px;">
            Demo: 081234567890 · 082345678901 · 083456789012
          </div>`:`
          <div class="mb14">
            <label class="label">Nama Lengkap</label>
            <input class="input" id="rf-name" value="${S.regForm.name}" placeholder="Masukkan nama lengkap" />
          </div>
          <div class="mb14">
            <label class="label">Nomor HP</label>
            <input class="input" id="rf-phone" value="${S.regForm.phone}" placeholder="08xxxxxxxxxx" />
          </div>
          <div class="mb14">
            <label class="label">Email (opsional)</label>
            <input class="input" id="rf-email" value="${S.regForm.email}" placeholder="email@contoh.com" />
          </div>
          <button class="btn block lg" onclick="handleRegister()">Daftar Sekarang</button>`}
        <div style="border-top:1px solid #F1F5F9;margin-top:20px;padding-top:16px;text-align:center;">
          <button style="background:none;border:none;color:#64748B;font-size:13px;cursor:pointer;font-family:inherit;" onclick="setPage('staff-login')">🔑 Masuk sebagai Karyawan →</button>
        </div>
      </div>
    </div>`;
}

function renderStaffLogin(){
  return `
    <div style="max-width:400px;margin:0 auto;">
      <div class="card">
        <div style="text-align:center;margin-bottom:24px;">
          <div style="font-size:56px;margin-bottom:8px;">🔑</div>
          <div style="font-weight:900;font-size:22px;color:#1E293B;">Panel Karyawan</div>
          <div style="font-size:14px;color:#64748B;">Masuk dengan akun karyawan</div>
        </div>
        <div class="mb14">
          <label class="label">Username</label>
          <input class="input" id="sl-user" placeholder="Username karyawan" />
        </div>
        <div class="mb20">
          <label class="label">Password</label>
          <input class="input" id="sl-pass" type="password" placeholder="Password" onkeydown="if(event.key==='Enter') handleStaffLogin()" />
        </div>
        <button class="btn block lg" style="background:linear-gradient(135deg,#1E293B,#0F172A);" onclick="handleStaffLogin()">🔐 Masuk</button>
        <div style="font-size:12px;color:#94A3B8;text-align:center;margin-top:12px;">
          Demo: admin / cleanwave123 &nbsp;|&nbsp; karyawan1 / karyawan123
        </div>
        <div style="border-top:1px solid #F1F5F9;margin-top:16px;padding-top:14px;text-align:center;">
          <button style="background:none;border:none;color:#64748B;font-size:13px;cursor:pointer;font-family:inherit;" onclick="setPage('login')">← Kembali ke halaman pelanggan</button>
        </div>
      </div>
    </div>`;
}

// ═══════════════════════════════════════════════════════════
// ██████████ STAFF RENDER ██████████
// ═══════════════════════════════════════════════════════════
function renderStaff(){
  if(!S.staffAuth){ S.mode='customer'; render(); return; }

  const pendingTimbang=S.transactions.filter(t=>t.status==='menunggu-timbang').length;
  const pendingBayar  =S.transactions.filter(t=>t.status==='menunggu-bayar').length;
  const lowStk=lowStockCount();

  const sideItems=[
    {id:'dashboard', label:'Dashboard',   icon:'📊'},
    {id:'antrian',   label:'Antrian',     icon:'📋', badge: pendingTimbang+pendingBayar||0},
    {id:'inventaris',label:'Inventaris',  icon:'📦', badgeWarn: lowStk||0},
    {id:'ulasan',    label:'Ulasan',      icon:'💬'},
    {id:'pelanggan', label:'Pelanggan',   icon:'👥'},
    {id:'laporan',   label:'Laporan',     icon:'📈'},
  ];

  const staffPages={
    dashboard:renderStaffDashboard,
    antrian:renderStaffAntrian,
    inventaris:renderStaffInventaris,
    ulasan:renderStaffUlasan,
    pelanggan:renderStaffPelanggan,
    laporan:renderStaffLaporan,
  };
  const titleMap={
    dashboard:'Dashboard',antrian:'Manajemen Antrian',
    inventaris:'Inventaris Alat & Bahan',ulasan:'Ulasan Pelanggan',
    pelanggan:'Data Pelanggan',laporan:'Laporan',
  };
  const pageHtml=(staffPages[S.staffPage]||renderStaffDashboard)();

  document.getElementById('app').innerHTML=`
    <div class="s-app">
      <aside class="s-sidebar">
        <div class="s-brand">
          <div class="s-brand-name">🌊 CleanWave</div>
          <div class="s-brand-sub">Staff Panel</div>
        </div>
        <div style="padding:8px 0;flex:1;overflow-y:auto;">
          <div class="s-nav-section">Menu</div>
          ${sideItems.map(n=>`
            <div class="s-nav-item ${S.staffPage===n.id?'active':''}" onclick="setStaffPage('${n.id}')">
              <span class="s-nav-icon">${n.icon}</span>
              ${n.label}
              ${n.badge?`<span class="s-badge-pill">${n.badge}</span>`:''}
              ${n.badgeWarn?`<span class="s-badge-warn">⚠️${n.badgeWarn}</span>`:''}
            </div>`).join('')}
        </div>
        <div style="padding:16px;border-top:1px solid rgba(255,255,255,.08);">
          <div class="s-nav-item" onclick="staffLogout()">
            <span class="s-nav-icon">🚪</span> Keluar
          </div>
        </div>
      </aside>

      <div class="s-main">
        <div class="s-topbar">
          <div class="s-topbar-title">${titleMap[S.staffPage]||''}</div>
          <div class="s-topbar-right">
            <div style="font-size:13px;color:#64748B;">${new Date().toLocaleDateString('id-ID',{weekday:'long',day:'numeric',month:'long',year:'numeric'})}</div>
            <div class="s-staff-info">
              <div class="s-avatar">${S.staffAuth.name[0]}</div>
              <div>
                <div style="font-size:13px;font-weight:700;color:#0F172A;">${S.staffAuth.name}</div>
                <div style="font-size:11px;color:#64748B;text-transform:capitalize;">${S.staffAuth.role}</div>
              </div>
            </div>
          </div>
        </div>
        <div class="s-content">${pageHtml}</div>
      </div>
    </div>`;

  renderModal();
}

// ─── Staff: Dashboard ─────────────────────────────────────
function renderStaffDashboard(){
  const today=new Date().toISOString().slice(0,10);
  const todayTx=S.transactions.filter(t=>t.date===today);
  const todayRevenue=S.transactions.filter(t=>t.paidAt===today).reduce((s,t)=>s+(t.price||0),0);
  const avg=avgRating();
  const lowStk=lowStockCount();

  const stats=[
    {label:'Antrian Hari Ini',  val:todayTx.length,        icon:'📋', bg:'#EFF6FF', ic:'#3B82F6'},
    {label:'Menunggu Timbang',  val:S.transactions.filter(t=>t.status==='menunggu-timbang').length, icon:'⚖️', bg:'#FFFBEB', ic:'#F59E0B'},
    {label:'Menunggu Bayar',    val:S.transactions.filter(t=>t.status==='menunggu-bayar').length,   icon:'💳', bg:'#F5F3FF', ic:'#8B5CF6'},
    {label:'Sedang Diproses',   val:S.transactions.filter(t=>t.status==='diproses').length,         icon:'🫧', bg:'#EFF6FF', ic:'#0EA5E9'},
    {label:'Siap Diambil',      val:S.transactions.filter(t=>t.status==='selesai').length,          icon:'✅', bg:'#F0FDF4', ic:'#10B981'},
    {label:'Pendapatan Hari Ini',val:rp(todayRevenue),      icon:'💰', bg:'#F0FDF4', ic:'#059669'},
    {label:'Rating Rata-rata',  val:avg>0?avg+' ★':'Belum ada', icon:'⭐', bg:'#FFFBEB', ic:'#D97706'},
    {label:'Stok Menipis',      val:lowStk,                 icon:'⚠️', bg: lowStk>0?'#FEE2E2':'#F0FDF4', ic: lowStk>0?'#DC2626':'#10B981'},
  ];

  // Low stock alert
  const lowItems=S.inventory.filter(i=>{
    if(i.cat==='Mesin') return i.status && i.status!=='Aktif';
    return i.stock < i.minStock;
  });

  const recentTx=S.transactions.slice().sort((a,b)=>b.id-a.id).slice(0,5);

  return `
    ${lowItems.length>0?`
      <div class="alert-banner" style="margin-bottom:20px;">
        ⚠️ ${lowItems.length} item inventaris membutuhkan perhatian: 
        ${lowItems.slice(0,3).map(i=>i.name).join(', ')}${lowItems.length>3?` dan ${lowItems.length-3} lainnya`:''}
        <button class="btn sm danger" style="margin-left:auto;" onclick="setStaffPage('inventaris')">Lihat Inventaris</button>
      </div>`:''}

    <div class="grid4" style="margin-bottom:24px;">
      ${stats.map(s=>`
        <div class="stat-card">
          <div class="stat-icon" style="background:${s.bg};">${s.icon}</div>
          <div>
            <div class="stat-val" style="color:${s.ic};font-size:22px;">${s.val}</div>
            <div class="stat-label">${s.label}</div>
          </div>
        </div>`).join('')}
    </div>

    <div style="display:grid;grid-template-columns:1.6fr 1fr;gap:20px;">
      <div class="card">
        <div style="font-weight:700;font-size:16px;margin-bottom:16px;color:#0F172A;">Transaksi Terbaru</div>
        <table class="table">
          <thead><tr>${['Antrian','Pelanggan','Layanan','Status','Aksi'].map(h=>`<th class="th">${h}</th>`).join('')}</tr></thead>
          <tbody>
            ${recentTx.map(tx=>{
              const cust=S.customers.find(c=>c.id===tx.customerId);
              return `<tr>
                <td class="td" style="font-weight:800;color:#0369A1;">${tx.qNum}</td>
                <td class="td"><div style="font-weight:700;">${cust?.name||'-'}</div><div style="font-size:12px;color:#94A3B8;">${cust?.phone||''}</div></td>
                <td class="td" style="font-size:13px;">${tx.service}</td>
                <td class="td">${statusBadge(tx.status)}</td>
                <td class="td">${quickActionBtn(tx)}</td>
              </tr>`;}).join('')}
          </tbody>
        </table>
      </div>

      <div>
        <div class="card" style="margin-bottom:0;">
          <div style="font-weight:700;font-size:16px;margin-bottom:16px;color:#0F172A;">Ringkasan Status</div>
          ${['menunggu-timbang','menunggu-bayar','diproses','selesai','selesai-bayar'].map(st=>{
            const cnt=S.transactions.filter(t=>t.status===st).length;
            const cfg=STATUS_CFG[st];
            return `<div style="display:flex;align-items:center;justify-content:space-between;padding:10px 14px;border-radius:10px;margin-bottom:8px;background:#F8FAFC;">
              <span style="font-size:13px;font-weight:600;">${cfg.icon} ${cfg.label}</span>
              <span class="badge ${cfg.cls}">${cnt}</span>
            </div>`;}).join('')}
        </div>
      </div>
    </div>`;
}

function quickActionBtn(tx){
  if(tx.status==='menunggu-timbang') return `<button class="btn sm warning" onclick="openModal('input-berat',{txId:${tx.id}})">⚖️ Timbang</button>`;
  if(tx.status==='menunggu-bayar')   return `<button class="btn sm purple" onclick="openModal('konfirm-bayar',{txId:${tx.id}})">💳 Konfirm Bayar</button>`;
  if(tx.status==='diproses')         return `<button class="btn sm success" onclick="openModal('update-status',{txId:${tx.id}})">🔄 Update</button>`;
  if(tx.status==='selesai')          return `<button class="btn sm success" onclick="doUpdateStatus(${tx.id},'selesai-bayar')">📦 Selesai</button>`;
  return `<span style="font-size:12px;color:#94A3B8;">—</span>`;
}

// ─── Staff: Antrian ───────────────────────────────────────
function renderStaffAntrian(){
  const filter=S.antriFilter||'Semua';
  const txs=S.transactions
    .filter(t=>filter==='Semua'||t.status===filter)
    .sort((a,b)=>{
      const order={'menunggu-timbang':0,'menunggu-bayar':1,'diproses':2,'selesai':3,'selesai-bayar':4};
      return (order[a.status]??9)-(order[b.status]??9)||b.id-a.id;
    });

  const filterOpts=['Semua','menunggu-timbang','menunggu-bayar','diproses','selesai','selesai-bayar'];

  return `
    <div>
      <div style="display:flex;gap:8px;margin-bottom:20px;flex-wrap:wrap;">
        ${filterOpts.map(f=>`
          <button class="btn ${(S.antriFilter||'Semua')===f?'':'secondary'} sm" onclick="S.antriFilter='${f}';renderStaff()">
            ${f==='Semua'?'Semua':STATUS_CFG[f]?.icon+' '+(STATUS_CFG[f]?.label||f)}
            ${f!=='Semua'?`(${S.transactions.filter(t=>t.status===f).length})`:``}
          </button>`).join('')}
      </div>

      ${txs.length===0?`<div class="card" style="text-align:center;color:#94A3B8;padding:40px;"><div style="font-size:48px;margin-bottom:12px;">✅</div>Tidak ada antrian.</div>`:''}
      ${txs.map(tx=>{
        const cust=S.customers.find(c=>c.id===tx.customerId);
        const borderColors={'menunggu-timbang':'#F59E0B','menunggu-bayar':'#8B5CF6','diproses':'#0EA5E9','selesai':'#10B981','selesai-bayar':'#94A3B8'};
        return `
          <div class="queue-card" style="border-left-color:${borderColors[tx.status]||'#E2E8F0'};">
            <div class="queue-num">${tx.qNum}</div>
            <div class="queue-info">
              <div class="queue-name">${cust?.name||'-'}</div>
              <div class="queue-meta">
                📞 ${cust?.phone||'-'} &nbsp;·&nbsp;
                👕 ${tx.service} &nbsp;·&nbsp;
                ${tx.pickupMethod==='dijemput'?'🛵 Dijemput':'🏪 Mandiri'} &nbsp;·&nbsp;
                ${payLbl(tx.paymentMethod)}
                ${tx.kg?` &nbsp;·&nbsp; ⚖️ ${tx.kg} kg`:''}
                ${tx.detergent&&tx.detergent!=='-'?` &nbsp;·&nbsp; 🧴 ${tx.detergent}`:''}
                ${tx.machine?` &nbsp;·&nbsp; 🌀 ${tx.machine}`:''}
                ${tx.price?` &nbsp;·&nbsp; ${rp(tx.price)}`:''}
                ${tx.estimatedDone?`<br/>⏰ Est: ${fmtEst(tx.estimatedDone)}`:''}
                ${tx.address?`<br/>📍 ${tx.address}`:''}
                ${tx.notes?`<br/>📝 ${tx.notes}`:''}
              </div>
            </div>
            <div>
              ${statusBadge(tx.status)}
              <div class="queue-actions" style="margin-top:10px;">
                ${quickActionBtn(tx)}
                ${tx.status!=='selesai-bayar'?`<button class="btn sm secondary" onclick="openModal('update-status',{txId:${tx.id}})">🔄</button>`:''}
                <button class="btn sm secondary" onclick="openModal('invoice',{txId:${tx.id}})">🧾</button>
              </div>
            </div>
          </div>`;}).join('')}
    </div>`;
}

// ─── NEW: Staff: Inventaris ───────────────────────────────
function renderStaffInventaris(){
  const filter=S.invFilter||'Semua';
  const cats=['Semua','Deterjen','Pelembut','Peralatan','Mesin'];
  const items=S.inventory.filter(i=>filter==='Semua'||i.cat===filter);
  const lowItems=S.inventory.filter(i=>{
    if(i.cat==='Mesin') return i.status && i.status!=='Aktif';
    return i.stock < i.minStock;
  });

  // Summary stats
  const totalCat={};
  S.inventory.forEach(i=>{ totalCat[i.cat]=(totalCat[i.cat]||0)+1; });

  return `
    <div>
      ${lowItems.length>0?`
        <div class="alert-banner">
          ⚠️ Perlu Restok: ${lowItems.map(i=>`${i.name} (sisa ${i.cat==='Mesin'?i.status:i.stock+' '+i.unit})`).join(' · ')}
        </div>`:''}

      <!-- Summary cards -->
      <div class="grid4" style="margin-bottom:20px;">
        ${[
          {label:'Total Item',       val:S.inventory.length,  icon:'📦', bg:'#EFF6FF', ic:'#3B82F6'},
          {label:'Perlu Restok',     val:lowItems.length,     icon:'⚠️', bg: lowItems.length>0?'#FEE2E2':'#F0FDF4', ic: lowItems.length>0?'#DC2626':'#10B981'},
          {label:'Jenis Deterjen',   val:totalCat['Deterjen']||0, icon:'🧴', bg:'#FFFBEB', ic:'#D97706'},
          {label:'Mesin Aktif',      val:S.inventory.filter(i=>i.cat==='Mesin'&&(i.status==='Aktif'||!i.status)).length, icon:'🌀', bg:'#F0FDF4', ic:'#059669'},
        ].map(s=>`
          <div class="stat-card">
            <div class="stat-icon" style="background:${s.bg};">${s.icon}</div>
            <div><div class="stat-val" style="color:${s.ic};font-size:22px;">${s.val}</div><div class="stat-label">${s.label}</div></div>
          </div>`).join('')}
      </div>

      <!-- Filter tabs -->
      <div style="display:flex;gap:8px;margin-bottom:20px;flex-wrap:wrap;">
        ${cats.map(c=>`
          <button class="btn ${(S.invFilter||'Semua')===c?'':'secondary'} sm" onclick="S.invFilter='${c}';renderStaff()">
            ${c==='Semua'?'🗂️ Semua':
              c==='Deterjen'?'🧴 Deterjen':
              c==='Pelembut'?'💧 Pelembut':
              c==='Peralatan'?'🪝 Peralatan':
              '🌀 Mesin'}
            (${c==='Semua'?S.inventory.length:S.inventory.filter(i=>i.cat===c).length})
          </button>`).join('')}
      </div>

      <!-- Items -->
      ${items.map(item=>{
        const st=getStockStatus(item);
        const pct=item.cat==='Mesin'
          ? (item.status==='Aktif'?100:item.status==='Maintenance'?50:0)
          : Math.min(100, (item.stock/Math.max(1,item.minStock*2))*100);
        const barColor={ok:'#10B981',warn:'#F59E0B',low:'#EF4444'}[st];
        return `
          <div class="inv-card" style="border-left-color:${barColor};">
            <div class="inv-icon">${item.icon}</div>
            <div class="inv-info">
              <div class="inv-name">${item.name}</div>
              <div class="inv-meta">
                ${item.cat==='Mesin'?`
                  Status: <strong>${item.status||'Aktif'}</strong> · Maintenance terakhir: ${item.lastMaint||'-'}
                `:`
                  Stok: <strong>${item.stock} ${item.unit}</strong> · Min stok: ${item.minStock} ${item.unit}
                  ${item.note?` · 📝 ${item.note}`:''}
                `}
              </div>
              <div class="inv-stock-bar">
                <div class="inv-stock-fill" style="width:${Math.max(3,pct)}%;background:${barColor};"></div>
              </div>
            </div>
            <div style="display:flex;flex-direction:column;align-items:flex-end;gap:8px;min-width:130px;">
              ${stockBadge(item)}
              <button class="btn sm outline" onclick="openModal('inv-edit',{invId:'${item.id}'})">✏️ Edit</button>
            </div>
          </div>`;}).join('')}
    </div>`;
}

// ─── NEW: Staff: Ulasan ───────────────────────────────────
function renderStaffUlasan(){
  const avg=avgRating();
  const sorted=[...S.ratings].sort((a,b)=>b.createdAt.localeCompare(a.createdAt));
  const filterStar=S.ulasanFilter||0;
  const filtered=filterStar?sorted.filter(r=>r.stars===filterStar):sorted;

  return `
    <div>
      <!-- Summary -->
      <div style="display:grid;grid-template-columns:auto 1fr;gap:20px;margin-bottom:24px;">
        <div class="card" style="text-align:center;min-width:180px;margin-bottom:0;">
          <div style="font-size:56px;font-weight:900;color:#D97706;line-height:1;">${avg||'—'}</div>
          <div style="font-size:22px;margin:8px 0;">${avg>0?renderStars(Math.round(avg),22):''}</div>
          <div style="font-size:13px;color:#64748B;font-weight:600;">${S.ratings.length} ulasan total</div>
        </div>
        <div class="card" style="margin-bottom:0;">
          <div style="font-weight:700;font-size:15px;margin-bottom:14px;color:#0F172A;">Distribusi Rating</div>
          ${[5,4,3,2,1].map(s=>{
            const cnt=S.ratings.filter(r=>r.stars===s).length;
            const pct=S.ratings.length?Math.round(cnt/S.ratings.length*100):0;
            return `
              <div style="display:flex;align-items:center;gap:10px;margin-bottom:10px;">
                <span style="color:#D97706;font-weight:700;width:14px;font-size:14px;">${s}</span>
                <span style="color:#D97706;font-size:14px;">★</span>
                <div style="flex:1;background:#F1F5F9;border-radius:99px;height:10px;overflow:hidden;">
                  <div style="background:linear-gradient(135deg,#F59E0B,#D97706);height:10px;width:${pct}%;border-radius:99px;transition:width .5s;"></div>
                </div>
                <span style="color:#64748B;font-size:13px;width:40px;">${cnt} (${pct}%)</span>
                <button class="btn sm secondary" style="font-size:11px;padding:3px 8px;" onclick="S.ulasanFilter=S.ulasanFilter===${s}?0:${s};renderStaff()">
                  ${filterStar===s?'✓ Filter':'Filter'}
                </button>
              </div>`;}).join('')}
        </div>
      </div>

      ${filterStar?`
        <div style="background:#EFF6FF;border-radius:10px;padding:10px 16px;margin-bottom:16px;display:flex;align-items:center;justify-content:space-between;font-size:13px;font-weight:600;color:#1E40AF;">
          <span>Menampilkan ulasan bintang ${filterStar} (${filtered.length} ulasan)</span>
          <button class="btn sm secondary" onclick="S.ulasanFilter=0;renderStaff()">✕ Hapus Filter</button>
        </div>`:''}

      <div class="card">
        <div style="font-weight:700;font-size:16px;margin-bottom:16px;color:#0F172A;">
          Semua Ulasan ${filtered.length>0?`(${filtered.length})`:''}
        </div>
        ${filtered.length===0?`
          <div style="text-align:center;color:#94A3B8;padding:40px;">
            <div style="font-size:48px;margin-bottom:12px;">💬</div>
            ${S.ratings.length===0?'Belum ada ulasan dari pelanggan.':'Tidak ada ulasan dengan filter ini.'}
          </div>`:''}
        ${filtered.map(r=>{
          const cust=S.customers.find(c=>c.id===r.customerId);
          const tx=S.transactions.find(t=>t.id===r.txId);
          return `
            <div class="review-card">
              <div class="review-header">
                <div>
                  <div style="display:flex;align-items:center;gap:8px;">
                    <div class="review-name">${cust?.name||'Pelanggan'}</div>
                    <span style="font-size:12px;color:#64748B;">${cust?.phone||''}</span>
                  </div>
                  <div style="font-size:13px;margin-top:4px;">
                    ${renderStars(r.stars,16)}
                    <span class="badge ${r.stars>=4?'s-selesai':r.stars>=3?'s-proses':'s-timbang'}" style="font-size:11px;margin-left:6px;">
                      ${['','Sangat Buruk','Kurang','Cukup','Baik','Sangat Baik'][r.stars]}
                    </span>
                  </div>
                </div>
                <div style="text-align:right;">
                  <div class="review-date">${fmtEst(r.createdAt)}</div>
                  ${tx?`<div style="font-size:12px;color:#64748B;margin-top:4px;">${tx.qNum} · ${tx.service}</div>`:''}
                </div>
              </div>
              ${r.comment?`<div class="review-comment">"${r.comment}"</div>`:`<div style="font-size:12px;color:#94A3B8;font-style:italic;">Tidak ada komentar.</div>`}
            </div>`;}).join('')}
      </div>
    </div>`;
}

// ─── Staff: Pelanggan ─────────────────────────────────────
function renderStaffPelanggan(){
  return `
    <div>
      <div class="card">
        <div style="font-weight:700;font-size:16px;margin-bottom:16px;color:#0F172A;">Data Pelanggan (${S.customers.length})</div>
        <table class="table">
          <thead><tr>${['Nama','No. HP','Bergabung','Tier','Poin','Transaksi','Total Belanja','Rating'].map(h=>`<th class="th">${h}</th>`).join('')}</tr></thead>
          <tbody>
            ${S.customers.map(c=>{
              const t=getTier(c.pts);
              const myTx=S.transactions.filter(tx=>tx.customerId===c.id&&tx.status==='selesai-bayar');
              const total=myTx.reduce((s,tx)=>s+(tx.price||0),0);
              const custRatings=S.ratings.filter(r=>r.customerId===c.id);
              const custAvg=custRatings.length?(custRatings.reduce((s,r)=>s+r.stars,0)/custRatings.length).toFixed(1):null;
              return `<tr>
                <td class="td" style="font-weight:700;">${c.name}</td>
                <td class="td">${c.phone}</td>
                <td class="td" style="font-size:12px;color:#64748B;">${c.joinDate}</td>
                <td class="td"><span class="badge" style="background:${t.bg};color:${t.color};">${t.name} ★</span></td>
                <td class="td" style="font-weight:800;color:#D97706;">${c.pts} ⭐</td>
                <td class="td" style="text-align:center;">${S.transactions.filter(tx=>tx.customerId===c.id).length}</td>
                <td class="td" style="font-weight:700;color:#0369A1;">${rp(total)}</td>
                <td class="td">${custAvg?renderStars(Math.round(custAvg),13)+' <span style="font-size:12px;font-weight:700;">'+custAvg+'</span>':'<span style="color:#94A3B8;font-size:12px;">—</span>'}</td>
              </tr>`;}).join('')}
          </tbody>
        </table>
      </div>
    </div>`;
}

// ─── Staff: Laporan ───────────────────────────────────────
function renderStaffLaporan(){
  const done=S.transactions.filter(t=>t.paidAt);
  const totalRev=done.reduce((s,t)=>s+(t.price||0),0);
  const totalKg=S.transactions.filter(t=>t.kg).reduce((s,t)=>s+t.kg,0);
  const svcCount={};
  S.transactions.forEach(t=>{ svcCount[t.service]=(svcCount[t.service]||0)+1; });
  const avg=avgRating();

  return `
    <div>
      <div class="grid4" style="margin-bottom:20px;">
        ${[
          {label:'Total Pendapatan',   val:rp(totalRev),              icon:'💰',bg:'#F0FDF4',ic:'#059669'},
          {label:'Total Transaksi',    val:S.transactions.length,     icon:'📦',bg:'#EFF6FF',ic:'#3B82F6'},
          {label:'Total Cucian',       val:totalKg.toFixed(1)+' kg',  icon:'⚖️',bg:'#FFFBEB',ic:'#F59E0B'},
          {label:'Rata-rata Rating',   val:avg>0?avg+' ★':'—',        icon:'⭐',bg:'#FFFBEB',ic:'#D97706'},
        ].map(s=>`
          <div class="stat-card">
            <div class="stat-icon" style="background:${s.bg};">${s.icon}</div>
            <div><div class="stat-val" style="color:${s.ic};">${s.val}</div><div class="stat-label">${s.label}</div></div>
          </div>`).join('')}
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-bottom:20px;">
        <div class="card">
          <div style="font-weight:700;font-size:16px;margin-bottom:16px;color:#0F172A;">Popularitas Layanan</div>
          ${Object.entries(svcCount).sort((a,b)=>b[1]-a[1]).map(([svc,cnt])=>{
            const pct=Math.round(cnt/S.transactions.length*100);
            return `
              <div style="margin-bottom:14px;">
                <div style="display:flex;justify-content:space-between;font-size:14px;margin-bottom:6px;">
                  <span style="font-weight:600;">${svc}</span><span style="color:#64748B;">${cnt}x (${pct}%)</span>
                </div>
                <div style="background:#F1F5F9;border-radius:99px;height:8px;">
                  <div style="background:linear-gradient(135deg,#0EA5E9,#0369A1);height:8px;border-radius:99px;width:${pct}%;transition:width .5s;"></div>
                </div>
              </div>`;}).join('')}
        </div>

        <div class="card">
          <div style="font-weight:700;font-size:16px;margin-bottom:16px;color:#0F172A;">Metode Pembayaran</div>
          ${['cash','transfer','qris'].map(pm=>{
            const cnt=S.transactions.filter(t=>t.paymentMethod===pm).length;
            const pct=S.transactions.length?Math.round(cnt/S.transactions.length*100):0;
            return `
              <div style="margin-bottom:14px;">
                <div style="display:flex;justify-content:space-between;font-size:14px;margin-bottom:6px;">
                  <span style="font-weight:600;">${payLbl(pm)}</span><span style="color:#64748B;">${cnt}x (${pct}%)</span>
                </div>
                <div style="background:#F1F5F9;border-radius:99px;height:8px;">
                  <div style="background:linear-gradient(135deg,#10B981,#059669);height:8px;border-radius:99px;width:${pct}%;"></div>
                </div>
              </div>`;}).join('')}
        </div>
      </div>

      <div class="card">
        <div style="font-weight:700;font-size:16px;margin-bottom:16px;color:#0F172A;">Semua Transaksi</div>
        <div style="overflow-x:auto;">
          <table class="table">
            <thead><tr>${['Antrian','Pelanggan','Tgl','Layanan','Berat','Bayar','Status','Total','Poin','Rating'].map(h=>`<th class="th">${h}</th>`).join('')}</tr></thead>
            <tbody>
              ${S.transactions.slice().sort((a,b)=>b.id-a.id).map(tx=>{
                const cust=S.customers.find(c=>c.id===tx.customerId);
                const txRating=S.ratings.find(r=>r.txId===tx.id);
                return `<tr>
                  <td class="td" style="font-weight:800;color:#0369A1;">${tx.qNum}</td>
                  <td class="td"><div style="font-weight:600;">${cust?.name||'-'}</div><div style="font-size:11px;color:#94A3B8;">${cust?.phone||''}</div></td>
                  <td class="td" style="font-size:12px;color:#64748B;">${tx.date}</td>
                  <td class="td" style="font-size:13px;">${tx.service}</td>
                  <td class="td">${tx.kg?tx.kg+' kg':'—'}</td>
                  <td class="td" style="font-size:12px;">${payLbl(tx.paymentMethod)}</td>
                  <td class="td">${statusBadge(tx.status)}</td>
                  <td class="td" style="font-weight:700;color:#0369A1;">${tx.price!==null?rp(tx.price):'—'}</td>
                  <td class="td" style="color:#D97706;font-weight:600;">${tx.pts?'+'+tx.pts+'⭐':'—'}</td>
                  <td class="td">${txRating?renderStars(txRating.stars,13):'<span style="color:#94A3B8;font-size:12px;">—</span>'}</td>
                </tr>`;}).join('')}
            </tbody>
          </table>
        </div>
      </div>
    </div>`;
}

// ═══════════════════════════════════════════════════════════
// MAIN RENDER
// ═══════════════════════════════════════════════════════════
function render(){
  if(S.mode==='staff' && S.staffAuth){
    renderStaff();
    return;
  }
  document.getElementById('app').innerHTML=renderCustomerApp();
  renderModal();

  document.querySelectorAll('input,textarea').forEach(el=>{
    el.addEventListener('input',function(){
      if(this.id==='cs-query') S.checkStatusQuery=this.value;
    });
  });
}

// ═══════════════════════════════════════════════════════════
// INIT
// ═══════════════════════════════════════════════════════════
load();
if(S.loggedIn){
  S.orderForm.name=S.loggedIn.name;
  S.orderForm.phone=S.loggedIn.phone;
}
render();
</script>
</body>
</html>
