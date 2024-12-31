"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = require("express");
const sampleController_1 = require("../controllers/sampleController");
const router = (0, express_1.Router)();
router.get('/sample', sampleController_1.getSampleData);
exports.default = router;
