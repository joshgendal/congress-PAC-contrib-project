var proPublicaAPIKey = "qTt3VeYkzmY1n48Pc72sWN8VX0eCi5jwnNftwyTa";
var openSecretsAPIKey = "a8551db7eb798ce16ca3413e4cb6a30d";
var getLegislatorsURL = "http://www.opensecrets.org/api/?method=getLegislators";
var stateCodes = [
  {
    State: "Alabama",
    Abbrev: "Ala.",
    Code: "AL",
  },
  {
    State: "Alaska",
    Abbrev: "Alaska",
    Code: "AK",
  },
  {
    State: "Arizona",
    Abbrev: "Ariz.",
    Code: "AZ",
  },
  {
    State: "Arkansas",
    Abbrev: "Ark.",
    Code: "AR",
  },
  {
    State: "California",
    Abbrev: "Calif.",
    Code: "CA",
  },
  {
    State: "Colorado",
    Abbrev: "Colo.",
    Code: "CO",
  },
  {
    State: "Connecticut",
    Abbrev: "Conn.",
    Code: "CT",
  },
  {
    State: "Delaware",
    Abbrev: "Del.",
    Code: "DE",
  },
  {
    State: "District of Columbia",
    Abbrev: "D.C.",
    Code: "DC",
  },
  {
    State: "Florida",
    Abbrev: "Fla.",
    Code: "FL",
  },
  {
    State: "Georgia",
    Abbrev: "Ga.",
    Code: "GA",
  },
  {
    State: "Hawaii",
    Abbrev: "Hawaii",
    Code: "HI",
  },
  {
    State: "Idaho",
    Abbrev: "Idaho",
    Code: "ID",
  },
  {
    State: "Illinois",
    Abbrev: "Ill.",
    Code: "IL",
  },
  {
    State: "Indiana",
    Abbrev: "Ind.",
    Code: "IN",
  },
  {
    State: "Iowa",
    Abbrev: "Iowa",
    Code: "IA",
  },
  {
    State: "Kansas",
    Abbrev: "Kans.",
    Code: "KS",
  },
  {
    State: "Kentucky",
    Abbrev: "Ky.",
    Code: "KY",
  },
  {
    State: "Louisiana",
    Abbrev: "La.",
    Code: "LA",
  },
  {
    State: "Maine",
    Abbrev: "Maine",
    Code: "ME",
  },
  {
    State: "Maryland",
    Abbrev: "Md.",
    Code: "MD",
  },
  {
    State: "Massachusetts",
    Abbrev: "Mass.",
    Code: "MA",
  },
  {
    State: "Michigan",
    Abbrev: "Mich.",
    Code: "MI",
  },
  {
    State: "Minnesota",
    Abbrev: "Minn.",
    Code: "MN",
  },
  {
    State: "Mississippi",
    Abbrev: "Miss.",
    Code: "MS",
  },
  {
    State: "Missouri",
    Abbrev: "Mo.",
    Code: "MO",
  },
  {
    State: "Montana",
    Abbrev: "Mont.",
    Code: "MT",
  },
  {
    State: "Nebraska",
    Abbrev: "Nebr.",
    Code: "NE",
  },
  {
    State: "Nevada",
    Abbrev: "Nev.",
    Code: "NV",
  },
  {
    State: "New Hampshire",
    Abbrev: "N.H.",
    Code: "NH",
  },
  {
    State: "New Jersey",
    Abbrev: "N.J.",
    Code: "NJ",
  },
  {
    State: "New Mexico",
    Abbrev: "N.M.",
    Code: "NM",
  },
  {
    State: "New York",
    Abbrev: "N.Y.",
    Code: "NY",
  },
  {
    State: "North Carolina",
    Abbrev: "N.C.",
    Code: "NC",
  },
  {
    State: "North Dakota",
    Abbrev: "N.D.",
    Code: "ND",
  },
  {
    State: "Ohio",
    Abbrev: "Ohio",
    Code: "OH",
  },
  {
    State: "Oklahoma",
    Abbrev: "Okla.",
    Code: "OK",
  },
  {
    State: "Oregon",
    Abbrev: "Ore.",
    Code: "OR",
  },
  {
    State: "Pennsylvania",
    Abbrev: "Pa.",
    Code: "PA",
  },
  {
    State: "Rhode Island",
    Abbrev: "R.I.",
    Code: "RI",
  },
  {
    State: "South Carolina",
    Abbrev: "S.C.",
    Code: "SC",
  },
  {
    State: "South Dakota",
    Abbrev: "S.D.",
    Code: "SD",
  },
  {
    State: "Tennessee",
    Abbrev: "Tenn.",
    Code: "TN",
  },
  {
    State: "Texas",
    Abbrev: "Tex.",
    Code: "TX",
  },
  {
    State: "Utah",
    Abbrev: "Utah",
    Code: "UT",
  },
  {
    State: "Vermont",
    Abbrev: "Vt.",
    Code: "VT",
  },
  {
    State: "Virginia",
    Abbrev: "Va.",
    Code: "VA",
  },
  {
    State: "Washington",
    Abbrev: "Wash.",
    Code: "WA",
  },
  {
    State: "West Virginia",
    Abbrev: "W.Va.",
    Code: "WV",
  },
  {
    State: "Wisconsin",
    Abbrev: "Wis.",
    Code: "WI",
  },
  {
    State: "Wyoming",
    Abbrev: "Wyo.",
    Code: "WY",
  },
];

function getStateCodes() {
  codesArr = [];
  stateCodes.forEach((obj) => {
    codesArr.push(obj.Code);
  });
  return codesArr;
}

codes = getStateCodes();

codes.forEach((code) => {
  fetch(
    `${getLegislatorsURL}&id=${code}&apikey=${openSecretsAPIKey}&output=json`
  )
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log(data.response.legislator);
    })
    .catch((err) => console.log("error in getLegislatorURL error:", err));
});
