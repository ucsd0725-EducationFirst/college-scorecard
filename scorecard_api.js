var ScorecardRequest = function() {
    var api_key = "w8UC6PgtWN6vn1eAVhLraLW3xwpBlCkO6UnHy8zI";
    this.url = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=" + api_key;
    this.fields = new Array();

    this.onlyFields = function(fields) {
        this.url += "&_fields=" + fields;
        this.fields = fields.split(",");
        return this;
    };

    this.sortedBy = function(param) {
        this.url += "&_sort=" + param;
        return this;
    };

    this.radiusAround(zip, distance) {
        this.url += "&_zip=" + zip + "&_distance=" distance;
        return this;
    }

    this.get = function(callback) {
        var self = this;
        $.get(this.url)
        .done(function(data) {
            var meta = data.metadata;
            var results = data.results;
            var schools = [];
            results.forEach(function(data) {
                schools.push(new ScoreboardSchoolResult(data));
            });
            callback(schools);
        })
        .fail(function(error) {
            console.log(error);
        })
        return this;
    };
};

var ScoreboardSchoolResult = function(json) {
    this.raw = json;

    var toLookFor = [
        ["name", ["school", "name"]],
        ["url", ["school", "school_url"]],
        ["zipCode", ["school", "zip"]],
        ["city", ["school", "city"]],
        ["state", ["school", "state"]],
        ["region", ["school", "region_id"]],
        ["male", ["2014", "student", "demographics", "men"]],
        ["female", ["2014", "student", "demographics", "female_share"]]
    ];

    for (var i = 0; i < toLookFor.length; i++) {
        var property = toLookFor[i][0];
        var path = toLookFor[i][1];
        var result = json;
        var foundFlag = true;
        for (var j = 0; j < path.length; j++) {
            var element = path[j];
            try {
                result = result[element];
            } catch (err) {
                console.log(element, err);
                foundFlag = false;
                break;
            }
        }
        if (foundFlag) {
            this[property] = result;
        }
    }
}
