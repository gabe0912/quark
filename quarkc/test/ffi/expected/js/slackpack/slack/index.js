var _qrt = require("quark/quark_runtime.js");
var quark = require('quark').quark;
exports.quark = quark;
var event = require('./event/index.js');
exports.event = event;
var slackpack_md = require('../slackpack_md/index.js');
exports.slackpack_md = slackpack_md;
var quark = require('quark').quark;
exports.quark = quark;



// CLASS SlackHandler
/**
 * Event handler for slack events. All unhandled events
 * are delegated to onSlackEvent by default.
 */
function SlackHandler() {
    this.__init_fields__();
}
exports.SlackHandler = SlackHandler;

function SlackHandler__init_fields__() {}
SlackHandler.prototype.__init_fields__ = SlackHandler__init_fields__;
SlackHandler.slack_SlackHandler_ref = slackpack_md.Root.slack_SlackHandler_md;
function SlackHandler_onSlackEvent(event) {}
SlackHandler.prototype.onSlackEvent = SlackHandler_onSlackEvent;

function SlackHandler_onHello(hello) {}
SlackHandler.prototype.onHello = SlackHandler_onHello;

function SlackHandler_onSlackError(error) {}
SlackHandler.prototype.onSlackError = SlackHandler_onSlackError;

function SlackHandler_onMessage(message) {}
SlackHandler.prototype.onMessage = SlackHandler_onMessage;

// CLASS User
/**
 * A reference to a user.
 */

function User(client, user) {
    this.__init_fields__();
}
exports.User = User;

function User__init_fields__() {
    this.client = null;
    this.user = null;
}
User.prototype.__init_fields__ = User__init_fields__;
User.slack_User_ref = slackpack_md.Root.slack_User_md;
function User__getClass() {
    return "slack.User";
}
User.prototype._getClass = User__getClass;

function User__getField(name) {
    if (_qrt.equals((name), ("client"))) {
        return (this).client;
    }
    if (_qrt.equals((name), ("user"))) {
        return (this).user;
    }
    return null;
}
User.prototype._getField = User__getField;

function User__setField(name, value) {
    if (_qrt.equals((name), ("client"))) {
        (this).client = value;
    }
    if (_qrt.equals((name), ("user"))) {
        (this).user = value;
    }
}
User.prototype._setField = User__setField;

// CLASS Channel
/**
 * A reference to a channel.
 */

function Channel(client, channel) {
    this.__init_fields__();
}
exports.Channel = Channel;

function Channel__init_fields__() {
    this.client = null;
    this.channel = null;
}
Channel.prototype.__init_fields__ = Channel__init_fields__;
Channel.slack_Channel_ref = slackpack_md.Root.slack_Channel_md;
/**
 * Send a message to a channel.
 */
function Channel_send(message) {}
Channel.prototype.send = Channel_send;

function Channel__getClass() {
    return "slack.Channel";
}
Channel.prototype._getClass = Channel__getClass;

function Channel__getField(name) {
    if (_qrt.equals((name), ("client"))) {
        return (this).client;
    }
    if (_qrt.equals((name), ("channel"))) {
        return (this).channel;
    }
    return null;
}
Channel.prototype._getField = Channel__getField;

function Channel__setField(name, value) {
    if (_qrt.equals((name), ("client"))) {
        (this).client = value;
    }
    if (_qrt.equals((name), ("channel"))) {
        (this).channel = value;
    }
}
Channel.prototype._setField = Channel__setField;

// CLASS Client
/**
 * Represents a persistent connection to the slack service.
 */

function Client(runtime, token, handler) {
    this.__init_fields__();
}
exports.Client = Client;

function Client__init_fields__() {
    this.runtime = null;
    this.token = null;
    this.handler = null;
    this.event_id = null;
    this.socket = null;
}
Client.prototype.__init_fields__ = Client__init_fields__;
Client.slack_Client_ref = slackpack_md.Root.slack_Client_md;
Client.quark_Map_quark_String_quark_Object__ref = slackpack_md.Root.quark_Map_quark_String_quark_Object__md;
/**
 * Connect the client to the slack service.
 */
function Client_connect() {}
Client.prototype.connect = Client_connect;

function Client_request(request, params, handler) {}
Client.prototype.request = Client_request;

function Client_ws_connect(wsurl) {}
Client.prototype.ws_connect = Client_ws_connect;

function Client_ws_send(message) {}
Client.prototype.ws_send = Client_ws_send;

function Client_onWSConnected(socket) {}
Client.prototype.onWSConnected = Client_onWSConnected;

function Client_onWSClose(socket) {}
Client.prototype.onWSClose = Client_onWSClose;

function Client_onWSError(socket) {}
Client.prototype.onWSError = Client_onWSError;

function Client_construct(type) {
    return null;
}
Client.prototype.construct = Client_construct;

function Client_onWSMessage(socket, message) {}
Client.prototype.onWSMessage = Client_onWSMessage;

function Client_onHTTPResponse(request, response) {}
Client.prototype.onHTTPResponse = Client_onHTTPResponse;

function Client__getClass() {
    return "slack.Client";
}
Client.prototype._getClass = Client__getClass;

function Client__getField(name) {
    if (_qrt.equals((name), ("runtime"))) {
        return (this).runtime;
    }
    if (_qrt.equals((name), ("token"))) {
        return (this).token;
    }
    if (_qrt.equals((name), ("handler"))) {
        return (this).handler;
    }
    if (_qrt.equals((name), ("event_id"))) {
        return (this).event_id;
    }
    if (_qrt.equals((name), ("socket"))) {
        return (this).socket;
    }
    return null;
}
Client.prototype._getField = Client__getField;

function Client__setField(name, value) {
    if (_qrt.equals((name), ("runtime"))) {
        (this).runtime = value;
    }
    if (_qrt.equals((name), ("token"))) {
        (this).token = value;
    }
    if (_qrt.equals((name), ("handler"))) {
        (this).handler = value;
    }
    if (_qrt.equals((name), ("event_id"))) {
        (this).event_id = value;
    }
    if (_qrt.equals((name), ("socket"))) {
        (this).socket = value;
    }
}
Client.prototype._setField = Client__setField;

function Client_onWSInit(socket) {}
Client.prototype.onWSInit = Client_onWSInit;

function Client_onWSBinary(socket, message) {}
Client.prototype.onWSBinary = Client_onWSBinary;

function Client_onWSClosed(socket) {}
Client.prototype.onWSClosed = Client_onWSClosed;

function Client_onWSFinal(socket) {}
Client.prototype.onWSFinal = Client_onWSFinal;

function Client_onHTTPInit(request) {}
Client.prototype.onHTTPInit = Client_onHTTPInit;

function Client_onHTTPError(request, message) {}
Client.prototype.onHTTPError = Client_onHTTPError;

function Client_onHTTPFinal(request) {}
Client.prototype.onHTTPFinal = Client_onHTTPFinal;
