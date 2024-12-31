"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const sampleRoutes_1 = __importDefault(require("./routes/sampleRoutes"));
const logger_1 = __importDefault(require("./middlewares/logger"));
const app = (0, express_1.default)();
app.use(express_1.default.json());
app.use(logger_1.default);
app.use('/api', sampleRoutes_1.default);
app.get('/', (req, res) => {
    res.send('Hello, world!');
});
exports.default = app;
