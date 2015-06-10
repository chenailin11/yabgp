# Copyright 2015 Cisco Systems, Inc.
# All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

""" All BGP constant values """

# some handy things to know
BGP_MAX_PACKET_SIZE = 4096
BGP_MARKER_SIZE = 16  # size of BGP marker
BGP_HEADER_SIZE = 19  # size of BGP header, including marker
BGP_MIN_OPEN_MSG_SIZE = 29
BGP_MIN_UPDATE_MSG_SIZE = 23
BGP_MIN_NOTIFICATION_MSG_SIZE = 21
BGP_MIN_KEEPALVE_MSG_SIZE = BGP_HEADER_SIZE
BGP_TCP_PORT = 179
BGP_ROUTE_DISTINGUISHER_SIZE = 8

# BGP message types
BGP_OPEN = 1
BGP_UPDATE = 2
BGP_NOTIFICATION = 3
BGP_KEEPALIVE = 4
BGP_ROUTE_REFRESH = 5
BGP_CAPABILITY = 6
BGP_ROUTE_REFRESH_CISCO = 0x80

BGP_SIZE_OF_PATH_ATTRIBUTE = 2

# attribute flags, from RFC1771
BGP_ATTR_FLAG_OPTIONAL = 0x80
BGP_ATTR_FLAG_TRANSITIVE = 0x40
BGP_ATTR_FLAG_PARTIAL = 0x20
BGP_ATTR_FLAG_EXTENDED_LENGTH = 0x10


# SSA flags
BGP_SSA_TRANSITIVE = 0x8000
BGP_SSA_TYPE = 0x7FFF

# SSA Types
BGP_SSA_L2TPv3 = 1
BGP_SSA_mGRE = 2
BGP_SSA_IPSec = 3
BGP_SSA_MPLS = 4
BGP_SSA_L2TPv3_IN_IPSec = 5
BGP_SSA_mGRE_IN_IPSec = 6

# AS_PATH segment types
AS_SET = 1  # RFC1771
AS_SEQUENCE = 2  # RFC1771
AS_CONFED_SET = 4  # RFC1965 has the wrong values, corrected in
AS_CONFED_SEQUENCE = 3  # draft-ietf-idr-bgp-confed-rfc1965bis-01.txt

# OPEN message Optional Parameter types
BGP_OPTION_AUTHENTICATION = 1  # RFC1771
BGP_OPTION_CAPABILITY = 2  # RFC2842

# attribute types
BGPTYPE_ORIGIN = 1  # RFC1771
BGPTYPE_AS_PATH = 2  # RFC1771
BGPTYPE_NEXT_HOP = 3  # RFC1771
BGPTYPE_MULTI_EXIT_DISC = 4  # RFC1771
BGPTYPE_LOCAL_PREF = 5  # RFC1771
BGPTYPE_ATOMIC_AGGREGATE = 6  # RFC1771
BGPTYPE_AGGREGATOR = 7  # RFC1771
BGPTYPE_COMMUNITIES = 8  # RFC1997
BGPTYPE_ORIGINATOR_ID = 9  # RFC2796
BGPTYPE_CLUSTER_LIST = 10  # RFC2796
BGPTYPE_DPA = 11  # work in progress
BGPTYPE_ADVERTISER = 12  # RFC1863
BGPTYPE_RCID_PATH = 13  # RFC1863
BGPTYPE_MP_REACH_NLRI = 14  # RFC2858
BGPTYPE_MP_UNREACH_NLRI = 15  # RFC2858
BGPTYPE_EXTENDED_COMMUNITY = 16  # Draft Ramachandra
BGPTYPE_NEW_AS_PATH = 17  # draft-ietf-idr-as4bytes
BGPTYPE_NEW_AGGREGATOR = 18  # draft-ietf-idr-as4bytes
BGPTYPE_SAFI_SPECIFIC_ATTR = 19  # draft-kapoor-nalawade-idr-bgp-ssa-00.txt
BGPTYPE_TUNNEL_ENCAPS_ATTR = 23  # RFC5512
BGPTYPE_LINK_STATE = 99
BGPTYPE_ATTRIBUTE_SET = 128

#  VPN Route Target  #
BGP_EXT_COM_RT_0 = 0x0002  # Route Target,Format AS(2bytes):AN(4bytes)
BGP_EXT_COM_RT_1 = 0x0102  # Route Target,Format IPv4 address(4bytes):AN(2bytes)
BGP_EXT_COM_RT_2 = 0x0202  # Route Target,Format AS(4bytes):AN(2bytes)

# Route Origin (SOO site of Origin)
BGP_EXT_COM_RO_0 = 0x0003  # Route Origin,Format AS(2bytes):AN(4bytes)
BGP_EXT_COM_RO_1 = 0x0103  # Route Origin,Format IP address:AN(2bytes)
BGP_EXT_COM_RO_2 = 0x0203  # Route Origin,Format AS(2bytes):AN(4bytes)

# BGP Flow Spec
BGP_EXT_TRA_RATE = 0x8006  # traffic-rate 2-byte as#, 4-byte float
BGP_EXT_TRA_ACTION = 0x8007  # traffic-action bitmask
BGP_EXT_REDIRECT = 0x8008  # redirect 6-byte Route Target
BGP_EXT_TRA_MARK = 0x8009  # traffic-marking DSCP value

# BGP cost cummunity
BGP_EXT_COM_COST = 0x4301

# BGP link bandwith
BGP_EXT_COM_LINK_BW = 0x4004

# NLRI type as define in BGP flow spec RFC
BGPNLRI_FSPEC_DST_PFIX = 1  # RFC 5575
BGPNLRI_FSPEC_SRC_PFIX = 2  # RFC 5575
BGPNLRI_FSPEC_IP_PROTO = 3  # RFC 5575
BGPNLRI_FSPEC_PORT = 4  # RFC 5575
BGPNLRI_FSPEC_DST_PORT = 5  # RFC 5575
BGPNLRI_FSPEC_SRC_PORT = 6  # RFC 5575
BGPNLRI_FSPEC_ICMP_TP = 7  # RFC 5575
BGPNLRI_FSPEC_ICMP_CD = 8  # RFC 5575
BGPNLRI_FSPEC_TCP_FLAGS = 9  # RFC 5575
BGPNLRI_FSPEC_PCK_LEN = 10  # RFC 5575
BGPNLRI_FSPEC_DSCP = 11  # RFC 5575
BGPNLRI_FSPEC_FRAGMENT = 12  # RFC 5575

# BGP message Constants
VERSION = 4
PORT = 179
HDR_LEN = 19
MAX_LEN = 4096

# BGP messages type
MSG_OPEN = 1
MSG_UPDATE = 2
MSG_NOTIFICATION = 3
MSG_KEEPALIVE = 4
MSG_ROUTEREFRESH = 5
MSG_CISCOROUTEREFRESH = 128

# BGP Capabilities Support

SUPPORT_4AS = False
CISCO_ROUTE_REFRESH = False
NEW_ROUTE_REFRESH = False
GRACEFUL_RESTART = False

# AFI_SAFI mapping

AFI_SAFI_DICT = {
    (1, 1): 'ipv4',
    (1, 4): 'label_ipv4',
    (1, 128): 'vpnv4',
    (2, 1): 'ipv6',
    (2, 4): 'label_ipv6',
    (2, 128): 'vpnv6'
}

AFI_SAFI_STR_DICT = {
    'ipv4': (1, 1),
    'ipv6': (1, 2)
}

# BGP FSM State
ST_IDLE = 1
ST_CONNECT = 2
ST_ACTIVE = 3
ST_OPENSENT = 4
ST_OPENCONFIRM = 5
ST_ESTABLISHED = 6

# BGP Timer (seconds)
DELAY_OPEN_TIME = 10
ROUTE_REFRESH_TIME = 10
LARGER_HOLD_TIME = 4 * 60
CONNECT_RETRY_TIME = 30
IDLEHOLD_TIME = 30
HOLD_TIME = 120

stateDescr = {
    ST_IDLE: "IDLE",
    ST_CONNECT: "CONNECT",
    ST_ACTIVE: "ACTIVE",
    ST_OPENSENT: "OPENSENT",
    ST_OPENCONFIRM: "OPENCONFIRM",
    ST_ESTABLISHED: "ESTABLISHED"
}

# Notification error codes
ERR_MSG_HDR = 1
ERR_MSG_OPEN = 2
ERR_MSG_UPDATE = 3
ERR_HOLD_TIMER_EXPIRED = 4
ERR_FSM = 5
ERR_CEASE = 6

# Notification suberror codes
ERR_MSG_HDR_CONN_NOT_SYNC = 1
ERR_MSG_HDR_BAD_MSG_LEN = 2
ERR_MSG_HDR_BAD_MSG_TYPE = 3

ERR_MSG_OPEN_UNSUP_VERSION = 1
ERR_MSG_OPEN_BAD_PEER_AS = 2
ERR_MSG_OPEN_BAD_BGP_ID = 3
ERR_MSG_OPEN_UNSUP_OPT_PARAM = 4
ERR_MSG_OPEN_UNACCPT_HOLD_TIME = 6
ERR_MSG_OPEN_UNSUP_CAPA = 7  # RFC 5492
ERR_MSG_OPEN_UNKNO = 8

ERR_MSG_UPDATE_MALFORMED_ATTR_LIST = 1
ERR_MSG_UPDATE_UNRECOGNIZED_WELLKNOWN_ATTR = 2
ERR_MSG_UPDATE_MISSING_WELLKNOWN_ATTR = 3
ERR_MSG_UPDATE_ATTR_FLAGS = 4
ERR_MSG_UPDATE_ATTR_LEN = 5
ERR_MSG_UPDATE_INVALID_ORIGIN = 6
ERR_MSG_UPDATE_INVALID_NEXTHOP = 8
ERR_MSG_UPDATE_OPTIONAL_ATTR = 9
ERR_MSG_UPDATE_INVALID_NETWORK_FIELD = 10
ERR_MSG_UPDATE_MALFORMED_ASPATH = 11
ERR_MSG_UPDATE_UNKOWN_ATTR = 12

ATTRIBUTE_ID_2_STR = {
    1: 'ORIGIN',
    2: 'AS_PATH',
    3: 'NEXT_HOP',
    4: 'MULTI_EXIT_DISC',
    5: 'LOCAL_PREF',
    6: 'ATOMIC_AGGREGATE',
    7: 'AGGREGATOR',
    8: 'COMMUNITY',
    9: 'ORIGINATOR_ID',
    10: 'CLUSTER_LIST',
    14: 'MP_REACH_NLRI',
    15: 'MP_UNREACH_NLRI',
    16: 'EXTENDED_COMMUNITY',
    17: 'AS4_PATH',
    18: 'AS4_AGGREGATOR'
}

ATTRIBUTE_STR_2_ID = dict([(k, v) for (k, v) in ATTRIBUTE_ID_2_STR.items()])


WELL_KNOW_COMMUNITY_INT_2_STR = {
    0xFFFF0000: 'PLANNED_SHUT',
    0xFFFF0001: 'ACCEPT_OWN',
    0xFFFF0002: 'ROUTE_FILTER_TRANSLATED_v4',
    0xFFFF0003: 'ROUTE_FILTER_v4',
    0xFFFF0004: 'ROUTE_FILTER_TRANSLATED_v6',
    0xFFFF0005: 'ROUTE_FILTER_v6',
    0xFFFFFF01: 'NO_EXPORT',
    0xFFFFFF02: 'NO_ADVERTISE',
    0xFFFFFF03: 'NO_EXPORT_SUBCONFED',
    0xFFFFFF04: 'NOPEER'
}

WELL_KNOW_COMMUNITY_STR_2_INT = dict(
    [(r, l) for (l, r) in WELL_KNOW_COMMUNITY_INT_2_STR.items()])

TCP_MD5SIG_MAXKEYLEN = 80
SS_PADSIZE_IPV4 = 120
TCP_MD5SIG = 14
SS_PADSIZE_IPV6 = 100
SIN6_FLOWINFO = 0
SIN6_SCOPE_ID = 0


COMMUNITY_DICT = False